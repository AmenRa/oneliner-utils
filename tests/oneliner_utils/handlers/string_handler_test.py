import os

import pytest

from oneliner_utils import read, write


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return "black sabbath"


@pytest.fixture
def path():
    return "tests.txt"


# TESTS ========================================================================
def test_write_read(x, path):
    write(x, path)
    assert read(path) == x
    os.remove(path)
