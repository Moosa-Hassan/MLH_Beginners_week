import streamlit as st
import pandas as pd
from datetime import timezone
from green_cloud_moniter.api import ElectricityMapsClient, forecast_to_df
from green_cloud_moniter.core import recommend_best_windows

st.set_page_config(page_title="Green Cloud Monitor", layout="wide")

st.title("Green Cloud Monitor 🌿⚡️")

st.sidebar.header("Settings")
zone = st.sidebar.text_input("Zone (e.g., FR, DE)", value="FR")
window_hours = st.sidebar.number_input("Window size (hours)", min_value=1, max_value=8, value=1)
api_key = st.sidebar.text_input("(Optional) Electricity Maps API Key", value="", type="password")

client = ElectricityMapsClient(api_key=api_key if api_key else None)

st.markdown("---")

with st.spinner("Fetching data..."):
    current = client.get_current_intensity(zone=zone)
    forecast = client.get_forecast(zone=zone, hours=24)
    df = forecast_to_df(forecast)

col1, col2 = st.columns([1, 2])

if current:
    intensity = current.get("intensity") if isinstance(current, dict) else current
    timestamp = current.get("datetime") if isinstance(current, dict) else None
    col1.metric(label="Current carbon intensity (gCO2eq/kWh)", value=f"{intensity:.1f}", delta=None)
    if timestamp:
        col1.write(f"As of: {pd.to_datetime(timestamp).tz_convert(timezone.utc)}")
else:
    col1.write("No current intensity data available")

if not df.empty:
    df_plot = df.reset_index()
    df_plot["time_local"] = df_plot["time"].dt.tz_convert('UTC').dt.tz_convert(None)
    df_plot = df_plot.set_index("time_local")
    col2.line_chart(df_plot["intensity"])

    recommendations = recommend_best_windows(df, window_hours=window_hours, top_n=3)
    st.subheader("Best times to run heavy tasks ✅")
    if recommendations:
        for start, end, avg in recommendations:
            st.write(f"{start.strftime('%Y-%m-%d %H:%M')} to {end.strftime('%Y-%m-%d %H:%M')} — avg {avg:.1f} gCO2eq/kWh")
    else:
        st.write("No recommendations available")
else:
    st.write("No forecast data available. Try demo mode or supply a valid API key.")

st.markdown("---")
st.caption("Demo mode uses bundled sample data when no API key is provided. For production, provide an Electricity Maps API key in the sidebar or via environment variable ELECTRICITY_MAPS_API_KEY.")
