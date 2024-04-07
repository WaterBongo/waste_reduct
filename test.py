import requests

r =requests.get("http://localhost:8080/product_stabilitiy/apple/iphone").json()
print(r)