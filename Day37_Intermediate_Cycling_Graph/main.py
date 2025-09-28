import requests
from datetime import datetime

USERNAME = "chiragdhawan" # Make your own username
TOKEN = "dh45df15g2g5442554458df59k0l" # Make your own token

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

# Step 1: Create a graph (run once to set up)
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Step 2: Add a pixel (log today’s cycling distance)
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": input("🚴 How many kilometers did you cycle today? ")
}
# requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

# Step 3: Update today’s pixel (optional)
update_endpoint = f"{pixel_creation_endpoint}/{today}"
new_pixel_data = {
    "quantity": "30.0"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)
