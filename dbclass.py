from pymongo import MongoClient
import datetime

class DBcomm:
    def __init__(self, ipadd, port, dbname):
        self.ipadd = ipadd
        self.port = port
        self.dbname = dbname
        self.mongo = MongoClient('mongodb://' + self.ipadd + ':' + self.port + '/')
        self.mongodb = self.mongo[dbname]

    def getPubkey(self, username):
        mongokey = self.mongodb.key
        pubkey = mongokey.find_one({'owner': username})
        return pubkey['pubKey']

    def setPubkey(self, username, pub_key):
        mongokey = self.mongodb.key
        if not mongokey.find_one({'owner': username}):
            mydict = {"owener": username, "pubkey": pub_key}
            mongokey.insert_one(mydict)

    def setTask(self):
        pass
    def setMessage(self, username, message, sender):
        mongokey = self.mongodb.messages
        mydict = {"owner": username, "message": message, "sender": sender, "time": str(datetime.datetime.now())}
        mongokey.insert_one(mydict)



