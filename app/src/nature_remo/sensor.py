from dataclasses import dataclass
import requests
import os

nature_access_token = os.environ['NATURE_ACCESS_TOKEN']

@dataclass
class SensorData():
    temperature: float
    humidity: int
    illumination: float

def fetch() -> SensorData:
    url = f'https://api.nature.global/1/devices'
    headers = {
        'Authorization': f'Bearer {nature_access_token}'
    }

    response = requests.get(url, headers=headers)
    json = response.json()
    newest_events = json[0]['newest_events']
    sensor_data = SensorData(
        temperature=newest_events["te"]['val'],
        humidity=newest_events["hu"]['val'],
        illumination=newest_events["il"]['val'])
    return sensor_data

def main() -> None:
    data = fetch()
    print(data)

if __name__ == "__main__":
    main()