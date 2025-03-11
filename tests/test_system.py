import pytest
from common import systems, processors, wires
from pybdp.system import load_system
from pybdp.processor import load_processor
from pybdp.wire import load_wire
from test_toolbox import toolbox


@pytest.fixture(scope="module")
def system(toolbox):
    processors_map = {}
    wires_map = {}
    for processor in processors:
        processors_map[processor["ID"]] = load_processor(
            processor, toolbox.blocks_map, toolbox.spaces_map
        )
    for wire in wires:
        wires_map[wire["ID"]] = load_wire(wire, processors_map, toolbox.spaces_map)
    return load_system(systems[0], processors_map, wires_map)


def test_load_system(system):
    assert system.id == "Sys1"
    assert system.name == "System 1"
    assert system.description == "My System"
    assert [processor.id for processor in system.processors] == ["P1", "P2", "P3"]
    assert [wire.id for wire in system.wires] == ["W1", "W2", "W3"]


def test_system_processors(system):
    assert len(system.processors) == 3
    assert system.processors[0].id == "P1"
    assert system.processors[1].id == "P2"
    assert system.processors[2].id == "P3"


def test_system_wires(system):
    assert len(system.wires) == 3
    assert system.wires[0].id == "W1"
    assert system.wires[1].id == "W2"
    assert system.wires[2].id == "W3"
