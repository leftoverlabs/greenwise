import requests

# Data to update in the PUT request
data = {
    "id": 1,
    "title": "updated title",
    "body": "updated body",
    "userId": 1
}

response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=data)

# Print the response
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
