from jsonschema import validate
from .schema import schema
from .toolbox import load_toolbox
from .workbench import load_workbench


class Project:
    def __init__(self, json: dict):
        self.raw_data = json
        self.toolbox = load_toolbox(json["Toolbox"])
        self.workbench = load_workbench(json["Toolbox"])
        self.blocks = self.toolbox.blocks
        self.spaces = self.toolbox.spaces

        print("Implement validation that there are no duplicate IDs")


def load_project(json: dict):
    validate(json, schema)
    return Project(json)
