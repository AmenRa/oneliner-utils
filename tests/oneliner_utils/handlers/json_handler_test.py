import os

import pytest

from oneliner_utils import read_json, write_json


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return {"band": "black sabbath", "genre": "doom"}


@pytest.fixture
def path():
    return "tests.json"


# TESTS ========================================================================
def test_write_read_json(x, path):
    write_json(x, path)
    assert read_json(path) == x
    os.remove(path)
