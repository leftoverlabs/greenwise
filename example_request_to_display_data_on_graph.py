import requests
import json
from datetime import datetime

# API endpoint
url = "https://api.leftoverlabs.com/graph/data/create/"

# Headers
headers = {
    "Content-Type": "application/json",
    "api-key": "hello-this-is-my-api-key",
    "dataset-id": "GjSwe3",
}

# Sensor data
data = {
    "sensor_value": "10"
}

# Send POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check response
if response.status_code == 200:
    print("Data posted successfully!")
else:
    print(f"Failed to post data: {response.status_code} - {response.text}")
