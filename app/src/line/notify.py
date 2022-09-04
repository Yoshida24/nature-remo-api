import requests

import os

def send(notification_message: str) -> requests.Response:
    line_notify_token = os.getenv('LINE_NOTIFY_TOKEN')
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': {notification_message}}
    return requests.post(line_notify_api, headers=headers, data=data)

def main() -> None:
    response = send('test message')
    print(response.json())

if __name__ == "__main__":
    main()