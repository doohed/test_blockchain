from blockchain.blockchain import Blockchain
from wallet.wallet import Wallet

def main():
    # Create blockchain
    blockchain = Blockchain()

    # Create wallets
    wallet1 = Wallet()
    wallet2 = Wallet()

    # Create and add a transaction
    transaction1 = wallet1.create_transaction(wallet2.public_key, 50)
    blockchain.add_transaction(transaction1)

    # Mine the pending transactions
    blockchain.mine_pending_transactions(wallet1.public_key)

    print(f"Is the blockchain valid? {blockchain.is_chain_valid()}")

    # Print all blocks
    for block in blockchain.chain:
        print(f"Block {block.index}: {block.hash}, Transactions: {len(block.transactions)}")

if __name__ == "__main__":
    main()

