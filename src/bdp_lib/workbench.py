from .processor import load_processor
from .wire import load_wire
from .system import load_system


class Workbench:
    def __init__(self, json: dict, blocks_map, spaces_map):
        self.raw_data = json
        self.processors = [
            load_processor(processor, blocks_map, spaces_map)
            for processor in json["Processors"]
        ]

        self.processors_map = {processor.id: processor for processor in self.processors}

        self.wires = [
            load_wire(wire, self.processors_map, spaces_map) for wire in json["Wires"]
        ]
        self.systems = [load_system(system) for system in json["Systems"]]

        print("Work bench ID validation")

    def __repr__(self):
        return """<Workbench
Processors: {}
Wires: {}
Systems: {} >""".format(
            [x.name for x in self.processors],
            [x.name for x in self.wires],
            [x.name for x in self.systems],
        )


def load_workbench(json: dict, blocks_map, spaces_map):
    return Workbench(json, blocks_map, spaces_map)
