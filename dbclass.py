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
    def getUser(self, username):
        mongokey = self.mongodb.users
        if (mongokey.find_one({"owner": username})):
            return 0
        else:
            return 1
    def setTask(self):
        pass

    def getMessage(self, username):
        output = []
        mongokey = self.mongodb.messages
        for docs in mongokey.find({"owner": username}):
            docs.pop('_id')
            output.append(docs)
        return output

    def setMessage(self, username, message, sender):
        mongokey = self.mongodb.messages
        mydict = {"owner": username, "message": message, "sender": sender, "time": str(datetime.datetime.now())}
        if (mongokey.insert_one(mydict)):
            return 0

    def newUser(self, username, email, pubkey):
        userData = self.mongodb.users
        if userData.find_one({"owner": username}):
            return "user Already Existed !!!"
        userNew = {"owner": username, "email": email}
        userData.insert_one(userNew)
        keysData = self.mongodb.keys
        keyColl = {"owner": username, "pubkey": pubkey}
        keysData.insert_one(keyColl)


