import pandas as pd

def parse_historical_data(data):
    """Parse historical data into a user-friendly format."""
    history = data["history"]
    df = pd.DataFrame(history)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df.to_dict(orient="records")
