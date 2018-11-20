import gnupg
import os

class Crypto:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.gpg = gnupg.GPG(gnupghome='./key')
        if not os.listdir(self.gpg.gnupghome):
            init_key = self.gpg.gen_key_input(key_type="RSA", key_length=2048, name_real=self.username, name_email=self.email)
            self.gpg.gen_key(init_key)

    def import_keys(self, pubkey):
        self.gpg.import_keys(pubkey)

    def export_public(self):
        return self.gpg.export_keys(keyids=self.email)

    def encryptdata(self, input_enc_data, user):
        encrypted_ascii_data = str(self.gpg.encrypt(input_enc_data, user))
        return encrypted_ascii_data

    def decryptdata(self, input_dec_data):
        decrypted_data = str(self.gpg.decrypt(input_dec_data))
        return decrypted_data

