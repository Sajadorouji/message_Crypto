import cryptograph
import os
from pymongo import MongoClient
import configparser
import json
import requests


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('mongodb.ini')
    mongo = MongoClient('mongodb://' + config['mongo']['IP'] + ':' + config['mongo']['PORT'] + '/')
    mydb = mongo.cryptoapi
    sajad = cryptograph.Crypto("sajad", "sajad.orj@gmail.com")

    print(os.listdir("./key"))


    mess = sajad.encryptdata("hello", "sajad")
    print(mess)

    URL = "http://127.0.0.1:5000/messages/sajad/list"
    location = "delhi technological university"
    r = requests.get(url=URL)
    data = r.json()
    print(data)

    print(sajad.decryptdata(mess))
    mongoget = mydb.users
    get_username = mongoget.find_one({'owner': 'sajad'})
    print(get_username["email"])

    # importing the requests library

    # your source code here
    source_code = ''' 
    print("Hello, world!") 
    a = 1 
    b = 2 
    print(a + b) 
    '''

    # data to be sent to api
    data = {'owner': API_KEY,
            'message': 'paste',
            'sender': source_code,
            'time': 'python'}

    # sending post request and saving response as response object
    r = requests.post(url=URL, data=data)

    # extracting response text
    pastebin_url = r.text
    print("The pastebin URL is:%s" % pastebin_url)

    #export = sajad.export_public()
    #print(export)


