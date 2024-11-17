import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code == 404:
    raise Exception("That resourse does not exist")
elif response.status_code == 401:
    raise Exception("You are not authorized to access this resource")