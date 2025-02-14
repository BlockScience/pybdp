class Workbench:
    def __init__(self, json: dict):
        self.raw_data = json


def load_workbench(json: dict):
    return Workbench(json)
