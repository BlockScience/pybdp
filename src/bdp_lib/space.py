class Space:
    def __init__(self, json: dict):
        self.raw_data = json


def load_space(json: dict):
    return Space(json)
