import json ,re
import requests
import rsacrypto
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

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
    publicFile = open("./publicKeys/pubkey" + user + ".key", "w")
    publicFile.write(pubkey.text)
    data = "I met aliens in UFO. Here is the map.".encode("utf-8")
    file_out = open("encrypted_data.bin", "wb")

    recipient_key = RSA.import_key(open("receiver.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]

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

    sajad = rsacrypto.RSAcrypt()
    sajad.generatekey()
    aaaa = sajad.encryptdata(b"sajadorouji")
    print(aaaa)
    bbb = sajad.decryptdata(aaaa)
    print(bbb)
    # get_messages()
    # set_messages('adp', b'helloThere', 'me')