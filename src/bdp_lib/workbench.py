from .processor import load_processor
from .wire import load_wire
from .system import load_system


class Workbench:
    def __init__(self, json: dict):
        self.raw_data = json
        self.processors = [
            load_processor(processor) for processor in json["Processors"]
        ]
        self.wires = [load_wire(wire) for wire in json["Wires"]]
        self.systems = [load_system(system) for system in json["Systems"]]


def load_workbench(json: dict):
    return Workbench(json)
