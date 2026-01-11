# Green Cloud Monitor 🌿⚡️

A small carbon-aware dashboard to display the current carbon intensity of your local grid and recommend the best times of day to run "heavy" tasks.

Features
- Query a carbon-intensity API (Electricity Maps) and show current intensity
- Show a short forecast (next 24 hours) and recommend the best hour(s) to run heavy tasks
- Demo / fallback mode when no API key is provided

Quick start
1. Create a virtual environment and install dependencies:

   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   pip install -r requirements.txt

2. (Optional) Set your Electricity Maps API key in an environment variable:

   set ELECTRICITY_MAPS_API_KEY=your_api_key_here

   Alternatively, you can enter the API key in the Streamlit sidebar at runtime.

3. Run locally with Streamlit:

   streamlit run streamlit_app.py

Running tests

- Run unit tests with pytest:

   pytest

Implementation notes

- The app uses `green_cloud_moniter/api.py` to fetch data. When no API key is provided the app runs in demo mode using bundled sample data (`green_cloud_moniter/sample_data.json`).
- The forecasting processing and recommendation logic live in `green_cloud_moniter/core.py`.

Integrations and next steps

- For production-grade carbon attribution and richer features, consider the Green Software Foundation's Carbon SDK and related projects: https://greensoftware.foundation/.
- You can easily swap in another carbon intensity provider by updating `api.py`.

License: MIT
