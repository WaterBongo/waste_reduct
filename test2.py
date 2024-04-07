import requests
print("hi")
r =requests.get("http://localhost:8052/get/Jane")
print(r.text)
