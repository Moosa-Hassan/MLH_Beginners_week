from datetime import timedelta
import pandas as pd


def recommend_best_windows(forecast_df: pd.DataFrame, window_hours: int = 1, top_n: int = 3):
    """Given a forecast DataFrame (index: datetime, column: intensity), return
    `top_n` windows with the lowest average intensity.

    Returns a list of tuples: (start_timestamp, end_timestamp, avg_intensity)
    """
    if forecast_df.empty:
        return []

    # Ensure hourly spaced data
    df = forecast_df.copy().resample('1H').mean().interpolate()

    results = []
    hours = len(df)
    for i in range(0, hours - window_hours + 1):
        window = df.iloc[i:i + window_hours]
        avg = float(window['intensity'].mean())
        start = window.index[0]
        end = window.index[-1] + pd.Timedelta(hours=1)
        results.append((start, end, avg))

    # sort by avg intensity
    results.sort(key=lambda x: x[2])
    return results[:top_n]
