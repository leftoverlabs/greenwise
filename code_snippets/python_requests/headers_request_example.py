import requests

# Custom headers
headers = {
    "Authorization": "Bearer YOUR_API_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)

# Print the response
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
