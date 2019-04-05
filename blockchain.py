import hashlib
import json
from time import time


class Blockchain():

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create a new genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain

        :param proof:
        :param previous_hash:
        :return:
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block


    def new_blcok(self):
        # Creates a new block and adds it to the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new block and adds it to the chain

        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Blcok that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1


    @staticmethod
    def hash(block):
        # Hashes a block
        """
        Creates a SHA-256 hash of a Block

        :param block:
        :return: <str>
        """

        ## We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns the last block in the chain
       return self.chain[-1]
