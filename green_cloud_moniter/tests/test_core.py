import pandas as pd
from datetime import datetime, timedelta
from green_cloud_moniter.core import recommend_best_windows


def test_recommend_best_windows_simple():
    # create a simple 5-hour forecast with clear minimum at hours 2-3
    now = datetime(2026, 1, 1, 0, 0)
    times = [now + timedelta(hours=i) for i in range(5)]
    intensities = [200, 150, 100, 160, 210]
    df = pd.DataFrame({"time": times, "intensity": intensities}).set_index("time")

    recs = recommend_best_windows(df, window_hours=1, top_n=2)
    assert len(recs) == 2
    assert recs[0][2] == 100  # lowest
    assert recs[0][0] == times[2]


if __name__ == "__main__":
    test_recommend_best_windows_simple()
    print("ok")
