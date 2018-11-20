import json
import requests
import configparser
import cryptograph


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def get_messages():
    URL = "http://127.0.0.1:5000/messages/sajad/list"

    response = requests.get(url=URL, headers=headers)

    if response.status_code == 200:
        print(response.json())
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


if __name__ == "__main__":
    get_messages()