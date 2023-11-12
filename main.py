import requests
from datetime import date

# Get today's date in the format YYYY-MM-DD
today_date = date.today().strftime("%Y-%m-%d")

# Construct the URL with today's date
url = f"https://www.nytimes.com/svc/wordle/v2/{today_date}.json"

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Extract and print the specific information
    print({
        "solution": data["solution"],
    })
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
