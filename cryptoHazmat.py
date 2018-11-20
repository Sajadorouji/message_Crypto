from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import os


class CryptoHazmat:
    def __init__(self, path):
        self.path = path
        self.private_key = ""
        self.publickey = ""

    def createKeysfile(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        if not os.path.isfile(self.path + "/privatekey.key"):
            self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
            self.publickey = self.private_key.public_key()
            privateFile = open(self.path + "/privatekey.key", "w")
            privateFile.write(str(self.private_key.private_bytes(encoding = serialization.Encoding.PEM, format = serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm = serialization.NoEncryption())))
            privateFile.close()
            publicFile = open(self.path + "/public.key", "w")
            publicFile.write(str(self.publickey.public_bytes(encoding = serialization.Encoding.PEM, format = serialization.PublicFormat.SubjectPublicKeyInfo)))
            publicFile.close()

    def encryptData(self, message):
        pass
    def decryptData(self, enc_message):
        pass




    # def printkey(self):
    #     # pem = self.private_key.private_bytes(encoding = serialization.Encoding.PEM, format = serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm = serialization.NoEncryption())
    #
    #     pem = self.publickey.public_bytes(encoding = serialization.Encoding.PEM, format = serialization.PublicFormat.SubjectPublicKeyInfo)
    #     return pem
    #

    # def







#
#
# >>> private_key = rsa.generate_private_key(
# ...     public_exponent=65537,
# ...     key_size=2048,
# ...     backend=default_backend()
#
#
# >>> with open("path/to/key.pem", "rb") as key_file:
# ...     private_key = serialization.load_pem_private_key(
# ...         key_file.read(),
# ...         password=None,
# ...         backend=default_backend()
# ...     )>>> message = b"encrypted data"
# >>> ciphertext = public_key.encrypt(
# ...     message,
# ...     padding.OAEP(
# ...         mgf=padding.MGF1(algorithm=hashes.SHA256()),
# ...         algorithm=hashes.SHA256(),
# ...         label=None
# ...     )
# ... )
# >>> plaintext = private_key.decrypt(
# ...     ciphertext,
# ...     padding.OAEP(
# ...         mgf=padding.MGF1(algorithm=hashes.SHA256()),
# ...         algorithm=hashes.SHA256(),
# ...         label=None
# ...     )
# ... )
# >>> plaintext == message
# True