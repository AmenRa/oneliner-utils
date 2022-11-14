import os
import types

import pytest

from oneliner_utils import read_list, write_list


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return ["black sabbath", "doom", "cannibal corpse", "death metal"]


@pytest.fixture
def path():
    return "tests.txt"


# TESTS ========================================================================
def test_write_read_list(x, path):
    write_list(x, path)
    assert read_list(path) == x
    os.remove(path)


def test_write_read_list_generator(x, path):
    write_list(x, path)
    y = read_list(path, generator=True)
    assert isinstance(y, types.GeneratorType)
    assert list(y) == x
    os.remove(path)
