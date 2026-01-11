import os
import json
from datetime import datetime, timedelta
import requests
import pandas as pd

BASE_URL = "https://api.electricitymaps.com/v3"
API_KEY = os.environ.get("ELECTRICITY_MAPS_API_KEY")


class ElectricityMapsClient:
    """Simple client to fetch current and forecast carbon intensity.

    If no `ELECTRICITY_MAPS_API_KEY` is defined, the client will fall back to
    bundled sample data to allow local demo mode.
    """

    def __init__(self, api_key=None):
        self.api_key = api_key or API_KEY
        self.session = requests.Session()
        if self.api_key:
            self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def _load_sample(self):
        sample_path = os.path.join(os.path.dirname(__file__), "sample_data.json")
        with open(sample_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_current_intensity(self, zone="FR"):
        """Return current intensity (gCO2eq/kWh) and timestamp for a zone.

        zone: ISO zone identifier (e.g., 'FR', 'DE', 'US-CA')
        """
        if not self.api_key:
            data = self._load_sample().get("current")
            return data

        # Best-effort attempt for ElectricityMaps endpoint
        url = f"{BASE_URL}/carbon-intensity/latest?zone={zone}"
        try:
            r = self.session.get(url, timeout=10)
            r.raise_for_status()
            return r.json()
        except Exception:
            # fallback
            return self._load_sample().get("current")

    def get_forecast(self, zone="FR", hours=24):
        """Return a forecast list of hourly intensities for the next `hours`.

        Returns a list of dicts with keys: timestamp (ISO str) and intensity (float)
        """
        if not self.api_key:
            return self._load_sample().get("forecast")[:hours]

        url = f"{BASE_URL}/carbon-intensity/forecast?zone={zone}&hours={hours}"
        try:
            r = self.session.get(url, timeout=10)
            r.raise_for_status()
            data = r.json()
            # Expecting data format: { "forecast": [ { "datetime": "...", "intensity": ... } , ... ] }
            if "forecast" in data:
                return data["forecast"]
            return data
        except Exception:
            return self._load_sample().get("forecast")[:hours]


# Utility to produce a DataFrame from the returned forecast
def forecast_to_df(forecast):
    """Convert forecast list to Pandas DataFrame with datetime index and intensity column."""
    rows = []
    for item in forecast:
        # support multiple shapes
        if isinstance(item, dict):
            ts = item.get("datetime") or item.get("timestamp") or item.get("time")
            intensity = item.get("intensity") or item.get("value") or item.get("carbonIntensity")
            rows.append({"time": ts, "intensity": intensity})
    df = pd.DataFrame(rows)
    df["time"] = pd.to_datetime(df["time"])
    df = df.set_index("time").sort_index()
    return df
