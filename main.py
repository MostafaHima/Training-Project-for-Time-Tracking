import requests
import os
from dotenv import load_dotenv
from datetime import datetime as dt

# Load environment variables from .env file
load_dotenv()

# User and API token configuration
USERNAME = "mostafahima"
API_TOKEN = os.getenv("PIXE_TOKEN")

# Endpoint for creating a user account
PIXELA_BASE_URL = "https://pixe.la/v1/users"
create_account_payload = {
    "token": API_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Send POST request to create a user account
create_account_response = requests.post(url=PIXELA_BASE_URL, json=create_account_payload)

# Endpoint for creating a graph
create_graph_url = f"{PIXELA_BASE_URL}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": API_TOKEN
}

# Payload for creating a graph
create_graph_payload = {
    "id": "first-graph",
    "name": "Test Tracking",
    "type": "float",
    "color": "ajisai",
    "unit": "hour",
    "timezone": "Africa/Cairo"
}

# Send POST request to create a graph
create_graph_response = requests.post(url=create_graph_url, json=create_graph_payload, headers=headers)

# Endpoint and payload for updating the graph unit
update_graph_url = f"{create_graph_url}/first-graph"
update_graph_payload = {
    "unit": "hour"
}

# Send PUT request to update graph unit
update_graph_response = requests.put(url=update_graph_url, headers=headers, json=update_graph_payload)

# Endpoint for adding a pixel to the graph
add_pixel_url = f"{create_graph_url}/first-graph"

# Get user input for today's tracking
hours_tracked = input("How many hours do you want to track?: ")
tracking_title = input("What is the title for today's activity?: ")
tracking_details = input("What did you accomplish today?: ")

# Payload for adding a pixel
add_pixel_payload = {
    "date": dt.today().strftime("%Y%m%d"),  # Current date in YYYYMMDD format
    "quantity": hours_tracked,
    "optionalData": f'{{"{tracking_title}": "{tracking_details}"}}'
}

# Send POST request to add a pixel
add_pixel_response = requests.post(url=add_pixel_url, headers=headers, json=add_pixel_payload)

# Print the response from the server
print(add_pixel_response.text)
