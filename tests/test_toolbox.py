from common import spaces, blocks
from pybdp.toolbox import Toolbox


def test_toolbox_spaces():
    json = {
        "Spaces": spaces,
        "Blocks": blocks,
    }
    toolbox = Toolbox(json)
    assert len(toolbox.spaces) == 5
    assert toolbox.spaces[0].id == "S1"
    assert toolbox.spaces[1].id == "S2"
    assert toolbox.spaces[2].id == "S3"
    assert toolbox.spaces[3].id == "S4"
    assert toolbox.spaces[4].id == "S5"
    assert str(toolbox.spaces[0]) == "< Space ID: S1 Name: A >"
    assert str(toolbox.spaces[1]) == "< Space ID: S2 Name: B >"
    assert str(toolbox.spaces[2]) == "< Space ID: S3 Name: C >"
    assert str(toolbox.spaces[3]) == "< Space ID: S4 Name: D >"
    assert str(toolbox.spaces[4]) == "< Space ID: S5 Name: E >"


def test_toolbox_blocks():
    json = {
        "Spaces": spaces,
        "Blocks": blocks,
    }
    toolbox = Toolbox(json)
    assert len(toolbox.blocks) == 3
    assert toolbox.blocks[0].id == "B1"
    assert toolbox.blocks[1].id == "B2"
    assert toolbox.blocks[2].id == "B3"
    assert str(toolbox.blocks[0]) == "< Block ID: B1 Name: Block 1 ['A', 'E']->['E']>"
    assert str(toolbox.blocks[1]) == "< Block ID: B2 Name: Block 2 ['E']->['C']>"
    assert str(toolbox.blocks[2]) == "< Block ID: B3 Name: Block 3 ['E', 'B']->['D']>"
