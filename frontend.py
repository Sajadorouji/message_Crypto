import json ,re
import requests
import cryptoHazmat


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
    pubkey = requests.get(url='http://127.0.0.1:5000/' + user + '/key', headers=headers)
    print(pubkey.text)
    # print(re.sub('b\'-----BEGIN PUBLIC KEY-----\\n', '', str(pubkey.text)))
    # print(b64data)
    # b64data = re.sub('b\'-----BEGIN PUBLIC KEY-----\\n', '', b64data)
    # print(b64data)
    encrypting = cryptoHazmat.CryptoHazmat('./')
    encryptedMSG = encrypting.encryptData(message, pubkey.text)
    print(encryptedMSG)

    # data = json.dumps({'owner': user,
    #         'message': encryptedMSG,
    #         'sender': sender,
    #         'time': str(datetime.datetime.now())})
    #
    # URL = "http://127.0.0.1:5000/messages/sajad/inbox"
    # r = requests.post(url=URL, data=data, headers=headers)
    #
    # # extracting response text
    # pastebin_url = r.text
    # print("The pastebin URL is:%s" % pastebin_url)

if __name__ == "__main__":

    # get_messages()
    set_messages('sajad', b'helloThere', 'me')