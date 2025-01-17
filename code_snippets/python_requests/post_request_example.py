import requests

# Data to send in the POST request
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

# Print the response
if response.status_code == 201:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
