class Toolbox:
    def __init__(self, json: dict):
        self.raw_data = json


def load_toolbox(json: dict):
    return Toolbox(json)
