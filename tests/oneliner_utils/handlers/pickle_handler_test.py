import os

import pytest

from oneliner_utils import read_pickle, write_pickle


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return {"band": "black sabbath", "genre": "doom"}


@pytest.fixture
def path():
    return "tests.pkl"


# TESTS ========================================================================
def test_write_read_pickle(x, path):
    write_pickle(x, path)
    assert read_pickle(path) == x
    os.remove(path)
