import requests as req

post_data = req.get("https://jsonplaceholder.typicode.com/posts")

users_data = req.get("https://jsonplaceholder.typicode.com/users")


p_data = post_data.json()
u_data = users_data.json()

users = {}
for u in u_data:
    users[u["id"]] = u["name"]

for p in p_data:
    print(f"{p["title"]} by {users[p["userId"]]}")