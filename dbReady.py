from pymongo import MongoClient
import configparser
import datetime


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('mongodb.ini')
    mongo = MongoClient('mongodb://' + config['mongo']['IP'] + ':' + config['mongo']['PORT'] + '/')
    mydb = mongo["cryptoapi"]
    collectionUsers = mydb["users"]
    collectionMessages = mydb["messages"]
    collectionKeys = mydb["keys"]
    collectionTasks = mydb["tasks"]
    mydict = {"owner": "sajad", "email": "sajad.orj@gmail.com"}
    collectionUsers.insert_one(mydict)
    mydict.clear()
    mydict = {"owner": "sajad", "message": """-----BEGIN PGP MESSAGE-----

hQEMA9HsxFJ7Ct5OAQgAikUK05vJqRQlRcH77NhWQcSwi0Iti/BgTk2fA0Tv/E3J
OnOtsvZRACz9JmHIlBb4hDAC8agPQ22Dl7u7Jje1QfbWAIAnVAnZW6N2afFlI6hE
WSSHVsbKknQ9qWG5dwIVmFTGF1LEDHyFG30aoUsjcr9a8nJcXVdvyC0tEf8LONVI
kmnMMkWy9MOgwi9rzVmx+/CVw6Ima7PDMN+b75UqnaT8tVbKJo/FgQ6/g8Wuk/xq
NPZ5j4198RynMBnZ4gIYZq+00m5Wy2MODTI2Oyo5PiINQgFZXTBAJqS2lgasPq0t
4AltqEOhORz6araqi0X0oX0qg7ck5sWF01adesWPgdJAAVN+TeQ6wKJHz3jXkr49
NGiWkE3+p5+xI5xb1xcqMjvX0p2954GJnJoTmXpmfqOy1kwwNJvHrtGbBPuXZTrD
YA==
=7EkU
-----END PGP MESSAGE-----""", "sender": "nobody", "time": str(datetime.datetime.now())}
    collectionMessages.insert_one(mydict)
    mydict.clear()
    mydict = {"owner": "sajad", "pubKey": "sajad.orj@gmail.com"}
    collectionKeys.insert_one(mydict)
    mydict.clear()
    mydict = {"owner": "sajad", "taskname": "first task", "taskDiscription": "nothing", "taskStatus": False}
    collectionTasks.insert_one(mydict)
    mydict.clear()
