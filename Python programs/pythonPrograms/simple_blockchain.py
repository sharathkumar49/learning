# Simple Blockchain Implementation
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        value = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block")

def next_block(last_block, data):
    return Block(last_block.index+1, last_block.hash, time.time(), data)

if __name__ == "__main__":
    blockchain = [create_genesis_block()]
    for i in range(1, 6):
        data = f"Block {i} data"
        block = next_block(blockchain[-1], data)
        blockchain.append(block)
        print(f"Block {block.index} Hash: {block.hash}")
