import requests

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

# Print status code
if response.status_code == 200:
    print("Resource deleted successfully.")
else:
    print(f"Error: {response.status_code}")
