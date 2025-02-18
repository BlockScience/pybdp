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
        self._add_processor_port_terminal_maps()
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

    def _add_processor_port_terminal_maps(self):
        self.processor_ports_map = {}
        self.processor_terminals_map = {}
        for processor in self.processors:
            self.processor_ports_map[processor] = [
                [] for _ in range(len(processor.ports))
            ]
            self.processor_terminals_map[processor] = [
                [] for _ in range(len(processor.terminals))
            ]

        for wire in self.wires:
            self.processor_terminals_map[wire.source["Processor"]][
                wire.source["Index"]
            ].append(wire)
            self.processor_ports_map[wire.target["Processor"]][
                wire.target["Index"]
            ].append(wire)

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
        # Check only one wire into each port
        filled_ports = set()
        for wire in self.wires:
            payload = (wire.target["Processor"].id, wire.target["Index"])
            assert (
                payload not in filled_ports
            ), "For system {} there are multiple wires pointing into the processor ID + index of {}, {}".format(
                self.name, payload[0], payload[1]
            )
            filled_ports.add(payload)

    def __repr__(self):
        return "< System Name: {} ID: {} Processors: {} Wires: {} >".format(
            self.name,
            self.id,
            [x.name for x in self.processors],
            [x.id for x in self.wires],
        )

    def get_open_ports(self):
        out = []
        for processor in self.processor_ports_map:
            for i, port_list in enumerate(self.processor_ports_map[processor]):
                if len(port_list) == 0:
                    out.append([processor, i, processor.ports[i]])
        return out

    def get_available_terminals(self, open_only=False):
        out = []
        for processor in self.processor_terminals_map:
            for i, terminal_list in enumerate(self.processor_terminals_map[processor]):
                if open_only:
                    if len(terminal_list) == 0:
                        out.append([processor, i, processor.terminals[i]])
                else:
                    out.append([processor, i, processor.terminals[i]])
        return out

    def make_processor_lazy(self):
        open_ports = self.get_open_ports()
        open_terminals = self.get_available_terminals(open_only=True)
        print(open_ports, open_terminals)


def load_system(json, processors_map, wires_map):
    return System(json, processors_map, wires_map)
