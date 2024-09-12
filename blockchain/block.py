import time
from utils.hash_utils import calculate_hash

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transactions_string = ''.join([tx.to_dict_str() for tx in self.transactions])
        block_data = f"{self.index}{self.previous_hash}{self.timestamp}{transactions_string}{self.nonce}"
        return calculate_hash(block_data)

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

