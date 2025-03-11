spaces = [
    {"ID": "S1", "Name": "A", "Description": "Space 1"},
    {"ID": "S2", "Name": "B"},
    {"ID": "S3", "Name": "C", "Description": "Space 3"},
    {"ID": "S4", "Name": "D"},
    {"ID": "S5", "Name": "E", "Description": "Space 5"},
]

blocks = [
    {
        "ID": "B1",
        "Name": "Block 1",
        "Description": "Block 1",
        "Domain": ["S1", "S5"],
        "Codomain": ["S5"],
    },
    {"ID": "B2", "Name": "Block 2", "Domain": ["S5"], "Codomain": ["S3"]},
    {"ID": "B3", "Name": "Block 3", "Domain": ["S5", "S2"], "Codomain": ["S4"]},
]

processors = [
    {
        "ID": "P1",
        "Name": "Processor 1",
        "Description": "Processor 1",
        "Parent": "B1",
        "Ports": ["S1", "S5"],
        "Terminals": ["S5"],
    },
    {
        "ID": "P2",
        "Name": "Processor 2",
        "Parent": "B2",
        "Ports": ["S5"],
        "Terminals": ["S3"],
    },
    {
        "ID": "P3",
        "Name": "Processor 3",
        "Parent": "B3",
        "Ports": ["S5", "S2"],
        "Terminals": ["S4"],
    },
]

wires = [
    {
        "ID": "W1",
        "Parent": "S5",
        "Source": {"Processor": "P1", "Index": 0},
        "Target": {"Processor": "P2", "Index": 0},
    },
    {
        "ID": "W2",
        "Parent": "S5",
        "Source": {"Processor": "P1", "Index": 0},
        "Target": {"Processor": "P3", "Index": 0},
    },
    {
        "ID": "W3",
        "Parent": "S5",
        "Source": {"Processor": "P1", "Index": 0},
        "Target": {"Processor": "P1", "Index": 1},
    },
]

systems = [
    {
        "ID": "Sys1",
        "Name": "System 1",
        "Description": "My System",
        "Processors": ["P1", "P2", "P3"],
        "Wires": ["W1", "W2", "W3"],
    }
]

project_json = {
    "Toolbox": {
        "Spaces": spaces,
        "Blocks": blocks,
    },
    "Workbench": {
        "Processors": processors,
        "Wires": wires,
        "Systems": systems,
    },
}
