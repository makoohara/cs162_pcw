import requests
import json
import uuid

# Base URL for httpbin.org
base_url = "http://httpbin.org"

# Task 1: Successfully log in using basic auth
print("Task 1: Successfully log in using basic auth")
username = "makoohara"
password = "1234567"
auth = (username, password)
response = requests.get(f"{base_url}/basic-auth/{username}/{password}", auth=auth)
print("Response for basic auth login:")
print(response.text)
print("\n")

# Task 2: Download an image
print("Task 2: Download an image")
image_url = f"{base_url}/image/png"
response = requests.get(image_url)
with open("downloaded_image.png", "wb") as file:
    file.write(response.content)
print("Image downloaded and saved as 'downloaded_image.png'")
print("\n")

# Task 3: Generate a UUID4
print("Task 3: Generate a UUID4")
generated_uuid = str(uuid.uuid4())
print(f"Generated UUID4: {generated_uuid}")
print("\n")

# Task 4: Return a simple JSON response
print("Task 4: Return a simple JSON response")
data = {"message": "Hello, httpbin!"}
response = requests.post(f"{base_url}/post", json=data)
print("Response for posting JSON data:")
print(json.dumps(response.json(), indent=4))
