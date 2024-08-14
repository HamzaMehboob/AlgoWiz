from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode

class ECCCrypto:
    def __init__(self):
        self.key = ECC.generate(curve='P-256')

    def get_public_key(self):
        return self.key.public_key().export_key(format='PEM')

    def sign(self, message):
        signer = DSS.new(self.key, 'fips-186-3')
        h = SHA256.new(message.encode())
        return b64encode(signer.sign(h)).decode()

    def verify(self, message, signature, public_key):
        pub_key = ECC.import_key(public_key)
        verifier = DSS.new(pub_key, 'fips-186-3')
        h = SHA256.new(message.encode())
        try:
            verifier.verify(h, b64decode(signature.encode()))
            return True
        except ValueError:
            return False
