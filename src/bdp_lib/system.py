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

    def _load_wires(self, wires, wires_map):
        pass

    def _check_ports(self):
        # Check only one wire into each port and warn if any ports are not filled
        pass


def load_system(json, processors_map, wires_map):
    return System(json, processors_map, wires_map)
