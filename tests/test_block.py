import sys
import pytest

sys.path.insert(0, "src")
from common import blocks, spaces
from pybdp.block import load_block
from pybdp.space import load_space


@pytest.fixture(scope="module")
def spaces_map():
    out = {}
    for space in spaces:
        out[space["ID"]] = load_space(space)
    return out


def test_load_block(spaces_map):
    block = load_block(blocks[0], spaces_map)
    assert block.id == "B1"
    assert block.name == "Block 1"
    assert block.description == "Block 1"
    assert block.domain == ["S1", "S5"]
    assert block.codomain == ["S5"]
    assert block.raw_data == blocks[0]

    block = load_block(blocks[1], spaces_map)
    assert block.id == "B2"
    assert block.name == "Block 2"
    assert block.description == None
    assert block.domain == ["S5"]
    assert block.codomain == ["S3"]
    assert block.raw_data == blocks[1]

    block = load_block(blocks[2], spaces_map)
    assert block.id == "B3"
    assert block.name == "Block 3"
    assert block.description == None
    assert block.domain == ["S5", "S2"]
    assert block.codomain == ["S4"]
    assert block.raw_data == blocks[2]
