class Processor:

    def __init__(self, json: dict, blocks_map: dict, spaces_map: dict):
        self.raw_data = json
        self.id = json["ID"]
        self.name = json["Name"]
        if "Description" in json:
            self.description = json["Description"]
        else:
            self.description = None

        self._load_parent(json["Parent"], blocks_map)
        self._load_ports(json["Ports"], spaces_map)
        self._load_terminals(json["Terminals"], spaces_map)

        if "Subsystem" in json:
            self.subsystem = json["Subsystem"]
            print("Implement subsystems")
        else:
            self.subsytem = None

    def _load_parent(self, parent, blocks_map):
        assert (
            parent in blocks_map
        ), "The parent block ID of {} is not valid for processor of {}".format(
            parent, self.name
        )
        self.parent = blocks_map[parent]

    def _load_ports(self, ports, spaces_map):
        bad_ports = [space for space in ports if space not in spaces_map]
        assert (
            len(bad_ports) == 0
        ), "The processor {} references port IDs of {} which are not valid port IDs".format(
            self.name, bad_ports
        )
        self.ports = [spaces_map[port] for port in ports]

        assert (
            self.ports == self.parent.domain
        ), "The ports of {} for the processor {} do not match the domain of {} that its parent block {} has".format(
            self.ports, self.name, self.parent.domain, self.parent.name
        )

    def _load_terminals(self, terminals, spaces_map):
        bad_terminals = [space for space in terminals if space not in spaces_map]
        assert (
            len(bad_terminals) == 0
        ), "The processor {} references terminal IDs of {} which are not valid port IDs".format(
            self.name, bad_terminals
        )
        self.terminals = [spaces_map[terminal] for terminal in terminals]

        assert (
            self.terminals == self.parent.codomain
        ), "The terminals of {} for the processor {} do not match the codomain of {} that its parent block {} has".format(
            self.terminals, self.name, self.parent.codomain, self.parent.name
        )

    def __repr__(self):
        return "< Processor ID: {} Name: {} {}->{}>".format(
            self.id,
            self.name,
            [x.name for x in self.ports],
            [x.name for x in self.terminals],
        )

    def get_shape(self):
        return self.parent


def load_processor(json, blocks_map, spaces_map):
    return Processor(json, blocks_map, spaces_map)
