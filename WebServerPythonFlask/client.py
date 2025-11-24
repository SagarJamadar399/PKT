import requests

# Send a GET request to the Flask server
url = "http://127.0.0.1:5000/"

response = requests.get(url)

print("Status code:", response.status_code)
print("Response headers:")
for k, v in response.headers.items():
    print(f"  {k}: {v}")

print("\nResponse body:")
print(response.text)
