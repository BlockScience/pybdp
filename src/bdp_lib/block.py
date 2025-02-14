class Block:
    def __init__(self, json: dict):
        self.raw_data = json
        self.id = json["ID"]
        self.name = json["Name"]
        if "Description" in json:
            self.description = json["Description"]
        else:
            self.description = None
        self.domain = json["Domain"]
        self.codomain = json["Codomain"]


def load_block(json: dict):
    return Block(json)
