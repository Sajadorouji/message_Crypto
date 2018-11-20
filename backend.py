from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
import cryptograph
import configparser

config = configparser.ConfigParser()
config.read('mongodb.ini')


app = Flask(__name__)
mongo = MongoClient('mongodb://' + config['mongo']['IP'] + ':' + config['mongo']['PORT'] + '/')
mongodb = mongo.cryptoapi


@app.route('/messages/<string:username>/list', methods=['GET'])
def get_messages(username):
    mongoget = mongodb.messages
    get_username = mongoget.find_one({'owner': username})
    output = []
    if get_username:
        cryptoinit = cryptograph.Crypto(username, email=get_username["email"])
        decryptmessage = cryptoinit.decryptdata(get_username['message'])
        output.append({'owner': get_username['owner'], 'enc_message': decryptmessage, 'sender': get_username['sender'], 'time': get_username['time']})
        return jsonify({'messages': output})
    else:
        print("Wrong User!!!")
        return abort(404)


@app.route('/messages/<string:username>/list', methods=['POST'])
def set_messages(username):
    mongoget = mongodb.messages
    get_username = mongoget.find_one({'owner': username})
    output = []
    if get_username:
        cryptoinit = cryptograph.Crypto(username, email=get_username["email"])
        encryptmessage = cryptoinit.encryptdata(get_username['message'], username)
        output.append({'owner': get_username['owner'], 'enc_message': encryptmessage, 'sender': get_username['sender'], 'time': get_username['time']})
        return jsonify({'messages': output})
    else:
        print("Wrong User!!!")
        return abort(404)


@app.route('/messages/<string:username>/key', methods=['GET'])
def get_user_key(username):

    mongoget = mongodb.tasks
    get_username = mongoget.find_one({'user': username})


@app.route('/messages/<string:username>/key', methods=['POST'])
def set_user_key(username, email):
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