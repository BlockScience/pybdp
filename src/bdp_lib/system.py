class System:
    def __init__(self, json: dict, processors_map: dict, wires_map: dict):
        self.raw_data = json
        self.id = json["ID"]
        self.name = json["Name"]
        if "Description" in json:
            self.description = json["Description"]
        else:
            self.description = None


def load_system(json, processors_map, wires_map):
    return System(json, processors_map, wires_map)
