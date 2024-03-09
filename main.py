import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

pixela_endpoint = 'https://pixe.la/v1/users'
PIXELA_TOKEN = os.environ.get('PIXELA_TOKEN')
PIXELA_USERNAME = os.environ.get('PIXELA_USERNAME')

user_params = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f'{pixela_endpoint}/{PIXELA_USERNAME}/graphs'

GRAPH_ID = 'graph1'
graph_params = {
    'id': GRAPH_ID,
    'name': 'Running Graph',
    'unit': 'mi',
    'type': 'float',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)




# The only part that does anything
pixel_creation_endpoint = f'{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now().strftime('%Y%m%d')

pixel_data = {
    'date': today,
    'quantity': input('How many miles did you run today? ')
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)





update_endpoint = f'{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{today}'

update_data = {
    'quantity': '5.0'
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

delete_endpoint = f'{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{date}'

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)