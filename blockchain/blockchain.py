from .block import Block
from transaction.transaction import Transaction
import time

class Blockchain:
    def __init__(self, difficulty=2, mining_reward=10):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.mining_reward = mining_reward
        self.pending_transactions = []

    def create_genesis_block(self):
        genesis_transaction = Transaction("SYSTEM", "genesis-address", 0)
        return Block(0, "0", time.time(), [genesis_transaction])

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        if not transaction.is_valid():
            raise Exception("Invalid transaction")
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address):
        reward_transaction = Transaction("SYSTEM", miner_address, self.mining_reward)
        self.pending_transactions.append(reward_transaction)

        block = Block(len(self.chain), self.get_latest_block().hash, time.time(), self.pending_transactions)
        block.mine_block(self.difficulty)

        self.chain.append(block)
        self.pending_transactions = []

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

