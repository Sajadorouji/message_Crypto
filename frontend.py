import json
import requests
import configparser
import cryptograph
import datetime

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
myusername = ''

def getUserdata(username):
    URL = "http://127.0.0.1:5000/messages/sajad/list"

    response = requests.get(url=URL, headers=headers)

    if response.status_code == 200:
        print(response.json())
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_messages():
    URL = "http://127.0.0.1:5000/messages/sajad/list"

    response = requests.get(url=URL, headers=headers)

    if response.status_code == 200:
        print(response.json())
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def set_messages(user, message, sender):
    data = json.dumps({'owner': user,
            'message': message,
            'sender': sender,
            'time': str(datetime.datetime.now())})

    URL = "http://127.0.0.1:5000/messages/sajad/inbox"
    r = requests.post(url=URL, data=data, headers=headers)

    # extracting response text
    pastebin_url = r.text
    print("The pastebin URL is:%s" % pastebin_url)

if __name__ == "__main__":

    get_messages()