class Wire:
    def __init__(self, json: dict, processors_map: dict, spaces_map: dict):
        self.raw_data = json
        self.id = json["ID"]
        self._load_parent(json["Parent"], spaces_map)
        self._load_source(json["Source"], processors_map)
        self._load_target(json["Target"], processors_map)

    def _load_parent(self, parent, spaces_map):
        assert (
            parent in spaces_map
        ), "The parent space ID of {} is not valid for wire of {}".format(
            parent, self.id
        )
        self.parent = spaces_map[parent]

    def _load_source(self, source, processors_map):
        assert (
            source["Processor"] in processors_map
        ), "The source processor ID of {} is not valid for wire of {}".format(
            source["Processor"], self.id
        )

    def _load_target(self, target, processors_map):
        assert (
            target["Processor"] in processors_map
        ), "The target processor ID of {} is not valid for wire of {}".format(
            target["Processor"], self.id
        )

    def __repr__(self):
        return "< Wire ID: {} Space: {} Source: Target: >".format(
            self.id, self.parent.name
        )


def load_wire(json, blocks_map, spaces_map):
    return Wire(json, blocks_map, spaces_map)
