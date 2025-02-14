from jsonschema import validate
from .schema import schema
from .toolbox import load_toolbox
from .workbench import load_workbench
from .convenience import find_duplicates


class Project:
    def __init__(self, json: dict):
        self.raw_data = json
        self.toolbox = load_toolbox(json["Toolbox"])
        self.workbench = load_workbench(json["Workbench"])
        self.blocks = self.toolbox.blocks
        self.spaces = self.toolbox.spaces

        self.processors = []
        self.wires = []
        self.systems = []

        # Bring in mapping
        self.blocks_map = self.toolbox.blocks_map
        self.spaces_map = self.toolbox.spaces_map
        self.toolbox_map = self.toolbox.toolbox_map

        self._validate_unique_ids()

    def _validate_unique_ids(self):
        duplicates = find_duplicates(
            self.blocks + self.spaces + self.processors + self.wires + self.systems
        )
        assert (
            len(duplicates) == 0
        ), f"Overlapping IDs between the toolbox and workbench found: {duplicates}"


def load_project(json: dict):
    validate(json, schema)
    return Project(json)
