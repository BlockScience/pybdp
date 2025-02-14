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

        # Bring in mapping
        self.blocks_map = self.toolbox.blocks_map
        self.spaces_map = self.toolbox.spaces_map
        self.toolbox_map = self.toolbox.toolbox_map

        print("Implement validation that there are no duplicate IDs")


def load_project(json: dict):
    validate(json, schema)
    return Project(json)
