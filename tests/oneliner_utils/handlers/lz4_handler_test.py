import os

import pytest

from oneliner_utils import read_lz4, write_lz4


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return "black sabbath".encode("utf-8")


@pytest.fixture
def y():
    return bytes([1, 2, 3, 4])


@pytest.fixture
def path():
    return "tests.bytes"


# TESTS ========================================================================
def test_write_read_lz4(x, path):
    write_lz4(x, path)
    assert read_lz4(path) == x
    os.remove(path)


def test_write_read_lz4_list(y, path):
    write_lz4(y, path)
    assert read_lz4(path) == y
    os.remove(path)
