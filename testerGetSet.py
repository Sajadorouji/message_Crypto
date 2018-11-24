import os, rsacrypto
import json ,re
import requests

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def createUser(username, email):
    sajad = rsacrypto.RSAcrypt()
    sajad.generatekey('./' + username)
    with open('./' + username + '/receiver.pem', 'r') as content_file:
        content = content_file.read()
    data = json.dumps({'owner': username,
            'email': email,
            'pubkey': str(content)})

    URL = "http://127.0.0.1:5000/newuser"
    r = requests.post(url=URL, data=data, headers=headers)
    print(r.text)
    return "true"

def testing(username, message):
    sajad = rsacrypto.RSAcrypt()

    aaaa = sajad.encryptdata(bytes(message, encoding='utf8'), './' + username + '/receiver.pem')
    print(aaaa)
    bbb = sajad.decryptdata(aaaa, './' + username + '/private.pem')
    print(bbb)

def getkeyAndEnc(username, message):
    pubkey = requests.get(url='http://127.0.0.1:5000/' + username + '/key', headers=headers)
    pubkeyfile = open('./tmppubkey.key', 'wb')
    print(pubkey.text)
    pubkeyfile.write(bytes(pubkey.text, encoding='utf8'))
    pubkeyfile.close()
    sajad = rsacrypto.RSAcrypt()
    aaaa = sajad.encryptdata(bytes(message, encoding='utf8'), './tmppubkey.key')
    print(aaaa)


if __name__ == "__main__":
    # testing('sajad', 'HelloIm Happy!!!!')
    # createUser('adp', 'adp@gmail.com')
    getkeyAndEnc("sajad","heelo dear!!!")
