import requests
api_url = "https://cat-fact.herokuapp.com/facts"

try:
    # Send a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response (assuming the API returns JSON)
        data = response.json()

        # Process the data as needed
        print("API Response:")
        print(data)
    else:
        print(f"Failed to retrieve data from the API. Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the API request: {e}")
