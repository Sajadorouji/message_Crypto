import cryptograph
import os
from pymongo import MongoClient
import configparser



if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('mongodb.ini')
    mongo = MongoClient('mongodb://' + config['mongo']['IP'] + ':' + config['mongo']['PORT'] + '/')
    mydb = mongo.cryptoapi
    sajad = cryptograph.Crypto("sajad", "sajad.orj@gmail.com")

    print(os.listdir("./key"))


    mess = sajad.encryptdata("hello", "sajad")
    print(mess)
    print(sajad.decryptdata(mess))
    mongoget = mydb.users
    get_username = mongoget.find_one({'owner': 'sajad'})
    print(get_username["email"])


    #export = sajad.export_public()
    #print(export)


