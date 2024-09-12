import json
from ecdsa import SigningKey, VerifyingKey, SECP256k1

class Transaction:
    def __init__(self, sender, receiver, amount, signature=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature

    def to_dict(self):
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount
        }

    def to_dict_str(self):
        return json.dumps(self.to_dict(), sort_keys=True)

    def sign_transaction(self, private_key):
        sk = SigningKey.from_string(bytes.fromhex(private_key), curve=SECP256k1)
        transaction_data = self.to_dict_str().encode()
        self.signature = sk.sign(transaction_data).hex()

    def is_valid(self):
        if self.sender == "SYSTEM":
            return True
        if not self.signature:
            return False
        transaction_data = self.to_dict_str().encode()
        vk = VerifyingKey.from_string(bytes.fromhex(self.sender), curve=SECP256k1)
        try:
            return vk.verify(bytes.fromhex(self.signature), transaction_data)
        except:
            return False

