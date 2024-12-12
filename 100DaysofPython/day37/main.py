import requests
from datetime import datetime

USERNAME= "fazilaroshan"
TOKEN="hahfiuwe7373s33"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID="graph1"
DATE_TODAY= datetime(year=2024, month=12, day=11)

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
# # authenticate our self through header
headers= {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


post_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixela_data={
    "date": DATE_TODAY.strftime("%Y%m%d"),
    "quantity": "15"
}
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_TODAY.strftime("%Y%m%d")}"

new_pixel_data={
    "quantity": "10"
}
# response = requests.put(url=put_endpoint, headers=headers, json=new_pixel_data)
# print(response.text)

remove_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_TODAY.strftime("%Y%m%d")}"
# response = requests.delete(url=remove_endpoint, headers=headers)
# print(response.text)
