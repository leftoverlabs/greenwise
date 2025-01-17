import requests

# Simple GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Print the response
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
