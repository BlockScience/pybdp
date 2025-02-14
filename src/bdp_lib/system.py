from .convenience import find_duplicates


class System:
    def __init__(self, json: dict, processors_map: dict, wires_map: dict):
        self.raw_data = json
        self.id = json["ID"]
        self.name = json["Name"]
        if "Description" in json:
            self.description = json["Description"]
        else:
            self.description = None

        self._load_processors(json["Processors"], processors_map)
        self._load_wires(json["Wires"], wires_map)
        self._check_ports()

    def _load_processors(self, processors, processors_map):
        bad_processors = [
            processor for processor in processors if processor not in processors_map
        ]
        assert (
            len(bad_processors) == 0
        ), "The system {} references processor IDs of {} which are not valid processor IDs".format(
            self.name, bad_processors
        )
        self.processors = [processors_map[processor] for processor in processors]

        # CHECK DUPLICATES
        duplicate_processors = find_duplicates(self.processors)
        assert (
            len(duplicate_processors) == 0
        ), f"Duplicate references to the same processor IDs found in system {self.name} (only load processors once in a system): {duplicate_processors}"

    def _load_wires(self, wires, wires_map):
        bad_wires = [wire for wire in wires if wire not in wires_map]
        assert (
            len(bad_wires) == 0
        ), "The system {} references wire IDs of {} which are not valid wire IDs".format(
            self.name, bad_wires
        )
        self.wires = [wires_map[wire] for wire in wires]

        # CHECK DUPLICATES
        duplicate_wire = find_duplicates(self.wires)
        assert (
            len(duplicate_wire) == 0
        ), f"Duplicate references to the same wire IDs found in system {self.name} (only load wires once in a system): {duplicate_wire}"

    def _check_ports(self):
        # Check only one wire into each port and warn if any ports are not filled
        pass

    def __repr__(self):
        return "< System Name: {} ID: {} Processors: {} Wires: {} >".format(
            self.name,
            self.id,
            [x.name for x in self.processors],
            [x.id for x in self.wires],
        )


def load_system(json, processors_map, wires_map):
    return System(json, processors_map, wires_map)
