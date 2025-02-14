from .space import load_space
from .block import load_block


class Toolbox:
    def __init__(self, json: dict):
        self.raw_data = json
        self.blocks = [load_block(block) for block in json["Blocks"]]
        self.spaces = [load_space(space) for space in json["Spaces"]]

        print("Replace spaces references with a _function")


def load_toolbox(json: dict):
    return Toolbox(json)
