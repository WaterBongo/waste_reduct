import requests
print("hi")
r =requests.get("http://localhost:8080/product_stabilitiy/google/app_management/GOOG")
print(r.text)