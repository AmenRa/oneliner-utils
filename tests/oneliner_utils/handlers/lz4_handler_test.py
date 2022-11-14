import os

import pytest

from oneliner_utils import read_lz4, write_lz4


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return "black sabbath"


@pytest.fixture
def y():
    return ["black sabbath", "doom", "cannibal corpse", "death metal"]


@pytest.fixture
def path():
    return "tests.txt"


# TESTS ========================================================================
def test_write_read_lz4(x, path):
    write_lz4(x, path)
    assert read_lz4(path) == x
    os.remove(path)


def test_write_read_lz4_list(y, path):
    write_lz4(y, path)
    assert read_lz4(path) == y
    os.remove(path)
