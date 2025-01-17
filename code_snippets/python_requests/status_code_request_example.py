import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    print(f"Request successful! Status code: {response.status_code}")
    print(response.json())
else:
    print(f"Request failed with status code: {response.status_code}")
