from .processor import load_processor
from .wire import load_wire
from .system import load_system
from .convenience import find_duplicates


class Workbench:
    def __init__(self, json: dict, blocks_map, spaces_map):
        self.raw_data = json

        # Load Processors
        self.processors = [
            load_processor(processor, blocks_map, spaces_map)
            for processor in json["Processors"]
        ]
        duplicate_processors = find_duplicates(self.processors)
        assert (
            len(duplicate_processors) == 0
        ), f"Duplicate processor IDs found: {duplicate_processors}"
        self.processors_map = {processor.id: processor for processor in self.processors}

        # Load Wire
        self.wires = [
            load_wire(wire, self.processors_map, spaces_map) for wire in json["Wires"]
        ]
        duplicate_wires = find_duplicates(self.wires)
        assert len(duplicate_wires) == 0, f"Duplicate wire IDs found: {duplicate_wires}"
        self.wires_map = {wire.id: wire for wire in self.wires}

        # Load systems
        self.systems = [
            load_system(system, self.processors_map, self.wires_map)
            for system in json["Systems"]
        ]

        print("Work bench ID validation")

    def __repr__(self):
        return """<Workbench
Processors: {}
Wires: {}
Systems: {} >""".format(
            [x.name for x in self.processors],
            [x.id for x in self.wires],
            [x.name for x in self.systems],
        )


def load_workbench(json: dict, blocks_map, spaces_map):
    return Workbench(json, blocks_map, spaces_map)
