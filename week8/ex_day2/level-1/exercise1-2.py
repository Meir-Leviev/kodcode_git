import requests
from fastapi import HTTPException
# response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# data = response.json()
# print(data['name'])
# print(data['email'])
# print(data['address']['city'])

# posts = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(len(posts.json()))

# user_2_p = requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")
# titles = user_2_p.json()

# for t in titles:
#     print(t['title'])

# ---------------------------------------------------------------------------------
# 2

def safe_get(url: str):
    req = requests.get(url)
    status = req.status_code
    if status == 200:
        return req.json()
    elif status == 404:
        return None
    
    raise HTTPException(status)

