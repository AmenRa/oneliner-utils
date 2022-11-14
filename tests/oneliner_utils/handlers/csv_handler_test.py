import os
import types

import pytest

from oneliner_utils import read_csv, write_csv


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return [
        {"band": "black sabbath", "genre": "doom"},
        {"band": "cannibal corpse", "genre": "death metal"},
    ]


@pytest.fixture
def path():
    return "tests.csv"


# TESTS ========================================================================
def test_write_read_csv(x, path):
    write_csv(x, path)
    assert read_csv(path) == x
    os.remove(path)


def test_write_read_csv_generator(x, path):
    write_csv(x, path)
    y = read_csv(path, generator=True)
    assert isinstance(y, types.GeneratorType)
    assert list(y) == x
    os.remove(path)
