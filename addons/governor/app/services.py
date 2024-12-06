import requests
from utils import parse_historical_data

BASE_URL = "http://supervisor/core/api"

def get_device_status(device_id):
    """Fetch current status of a device."""
    url = f"{BASE_URL}/states/{device_id}"
    headers = {"Authorization": "Bearer YOUR_LONG_LIVED_ACCESS_TOKEN"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_historical_data(device_id, start_date, end_date):
    """Fetch historical data for a device."""
    # Assuming Home Assistant keeps historical data in a database or integration
    # Replace this with actual implementation details.
    data = {
        "device_id": device_id,
        "history": [
            {"timestamp": start_date, "energy_usage": 5.5},
            {"timestamp": end_date, "energy_usage": 6.2},
        ],
    }
    return parse_historical_data(data)
