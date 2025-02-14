class Processor:

    def __init__(self, json: dict, blocks_map: dict, spaces_map: dict):
        self.raw_data = json
        self.id = json["ID"]
        self.name = json["Name"]
        if "Description" in json:
            self.description = json["Description"]
        else:
            self.description = None

        self.parent = self._load_parent(json["Parent"], blocks_map)
        self.ports = self._load_ports(spaces_map)
        self.terminals = self._load_terminals(spaces_map)

    def _load_parent(self, parent, blocks_map):
        assert (
            parent in blocks_map
        ), "The parent block ID of {} is not valid for processor of {}".format(
            parent, self.name
        )
        return None

    def _load_ports(self, spaces_map):
        return None

    def _load_terminals(self, spaces_map):
        return None


def load_processor(json, blocks_map, spaces_map):
    return Processor(json, blocks_map, spaces_map)
