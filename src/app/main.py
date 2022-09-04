import requests
import os
from pprint import pprint

nature_access_token = os.environ['NATURE_ACCESS_TOKEN']
nature_appearance = os.environ['NATURE_APPEARANCE']
url = f'https://api.nature.global/1/appliances/{nature_appearance}/aircon_settings'
headers = {
    'Authorization': f'Bearer {nature_access_token}'
}

response = requests.post(url, headers=headers, data={'button': ''})
pprint(response.json())
