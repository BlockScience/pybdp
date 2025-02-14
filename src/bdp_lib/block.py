class Block:
    def __init__(self, json: dict):
        self.raw_data = json


def load_block(json: dict):
    return Block(json)
