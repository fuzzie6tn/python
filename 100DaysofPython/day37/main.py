import requests
from datetime import datetime

USERNAME= "fazilaroshan"
TOKEN="hahfiuwe7373s33"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID="graph1"
date_today= datetime.now()

user_params= {
    "token": "hahfiuwe7373s33",
    "username": "fazilaroshan",
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config= {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "float",
    "color": "ajisai",
}
#
# # authenticate ourself through header
headers= {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint=f"{pixela_endpoint}{USERNAME}/graphs/{GRAPH_ID}"

parameters={
    "date": "20241212",
    "quantity": "5"
}

response = requests.post(url=post_pixel_endpoint, headers=headers, json=post_pixel_endpoint)
print(response.text)