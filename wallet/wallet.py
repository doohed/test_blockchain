from ecdsa import SigningKey, SECP256k1
from transaction.transaction import Transaction

class Wallet:
    def __init__(self):
        self.private_key = SigningKey.generate(curve=SECP256k1).to_string().hex()
        self.public_key = SigningKey.from_string(bytes.fromhex(self.private_key), curve=SECP256k1).verifying_key.to_string().hex()

    def create_transaction(self, receiver, amount):
        transaction = Transaction(self.public_key, receiver, amount)
        transaction.sign_transaction(self.private_key)
        return transaction

