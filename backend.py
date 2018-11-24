from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
import cryptograph
import dbclass
import configparser

config = configparser.ConfigParser()
config.read('mongodb.ini')


app = Flask(__name__)
mongo = MongoClient('mongodb://' + config['mongo']['IP'] + ':' + config['mongo']['PORT'] + '/')
mongodb = mongo.cryptoapi
newmongo = dbclass.DBcomm(config['mongo']['IP'], config['mongo']['PORT'], 'cryptoapi')

@app.route('/messages/<string:username>/list', methods=['GET'])
def get_messages(username):
    output = []
    get_username = newmongo.getUser(username)
    if get_username == 0:
        dataout = newmongo.getMessage(username)
        newmongo.closeCon()
        mongo.close()
        return jsonify({'messages': dataout})
    else:
        print("Wrong User!!!")
        return abort(404)


@app.route('/messages/<string:username>/inbox', methods=['POST'])
def set_messages(username):
    get_username = newmongo.getUser(username)
    if get_username == 0:
        content = request.get_json()
        print(content)
        x = newmongo.setMessage(content['owner'], content['message'], content['sender'])
        if x == 0:
            return "ok"
        else:
            return "not ok"
    else:
        print("Wrong User!!!")
        return abort(404)

@app.route('/newuser', methods=['POST'])
def createUser():
    content = request.get_json()
    x = newmongo.newUser(content['owner'], content['email'], content['pubkey'])
    if x:
        return "New User Created!!!"


@app.route('/<string:username>/key', methods=['GET'])
def get_user_key(username):

    mongoget = mongodb.keys
    get_username = mongoget.find_one({'owner': username})
    print(get_username)
    return get_username['pubKey']


@app.route('/messages/<string:username>/key', methods=['POST'])
def set_user_key(username, email):
    ### Strip fucking keys START AND END
    if not request.json or 'username' not in request.json:
        abort(400)
    mongopost = mongodb.keys
    cryptoinit = cryptograph.Crypto(username, email)
    jobpost = {
        'user': request.json['title'],
        'pubkey': request.json.get(cryptoinit.export_public(), ""),
    }
    mongopost.insert_one(jobpost)
    return jsonify(str(jobpost)), 201


if __name__ == '__main__':
    app.run(debug=True)