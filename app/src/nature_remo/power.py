import requests
import os

nature_access_token = os.environ['NATURE_ACCESS_TOKEN']
headers = {
    'Authorization': f'Bearer {nature_access_token}'
}

def url(nature_appearance: str) -> str:
    return f'https://api.nature.global/1/appliances/{nature_appearance}/aircon_settings'

def on(nature_appearance: str) -> None:
    requests.post(url(nature_appearance=nature_appearance), headers=headers, data={'button': ''})

def off(nature_appearance: str) -> None:
    requests.post(url(nature_appearance=nature_appearance), headers=headers, data={'button': 'power-off'})
