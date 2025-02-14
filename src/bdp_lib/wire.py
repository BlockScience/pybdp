class Wire:
    def __init__(self, json: dict, blocks_map: dict, spaces_map: dict):
        self.raw_data = json
        self.id = json["ID"]
        self._load_parent(json["Parent"], spaces_map)

    def _load_parent(self, parent, spaces_map):
        assert (
            parent in spaces_map
        ), "The parent space ID of {} is not valid for wire of {}".format(
            parent, self.id
        )
        self.parent = spaces_map[parent]

    def __repr__(self):
        return "< Wire ID: {} Space: {} Source: Target: >".format(
            self.id, self.parent.name
        )


def load_wire(json, blocks_map, spaces_map):
    return Wire(json, blocks_map, spaces_map)
