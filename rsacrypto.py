
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os, re


class RSAcrypt():
    def __init__(self):
        pass

    def generatekey(self, path='./key'):
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.isfile(path + "/private.pem"):
            key = RSA.generate(2048)
            private_key = key.export_key()
            file_out = open(path + "/private.pem", "wb")
            file_out.write(private_key)
            file_out.close()
            public_key = key.publickey().export_key()
            file_out = open(path + "/receiver.pem", "wb")
            file_out.write(public_key)
            file_out.close()
        return "OK"

    def encryptdata(self, input_enc_data, publickey='./key/receiver.pem'):
        recipient_key = RSA.import_key(open(publickey).read())
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(input_enc_data)
        return enc_session_key


    def decryptdata(self, input_dec_data, privatekey='./key/private.pem'):
        private_key = RSA.import_key(open(privatekey).read())
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(input_dec_data)
        return session_key.decode("utf-8")