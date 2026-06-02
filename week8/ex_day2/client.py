import requests
# Send a GET request to a public test API
response = requests.get("x")
print(response.status_code) # 200
print(response.json()) # returns a Python dict parsed from JSON
print(response.text) # returns the raw response as a string
# Access specific fields
data = response.json()
print(data["title"]) # the post title
print(data["userId"]) # the user who wrote it