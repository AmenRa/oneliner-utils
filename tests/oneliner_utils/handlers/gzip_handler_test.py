import os

import pytest

from oneliner_utils import (
    read_gzip,
    read_gzip_json_list,
    read_gzip_list,
    write_gzip,
    write_gzip_json_list,
    write_gzip_list,
)


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return "black sabbath"


@pytest.fixture
def y():
    return ["black sabbath", "doom", "cannibal corpse", "death metal"]


@pytest.fixture
def jsonl():
    return [
        {"band": "black sabbath", "genre": "doom"},
        {"band": "cannibal corpse", "genre": "death metal"},
    ]


@pytest.fixture
def path():
    return "tests.gzip"


# TESTS ========================================================================
def test_write_read_gzip(x, path):
    write_gzip(x, path)
    assert read_gzip(path) == x
    os.remove(path)


def test_write_read_gzip_list(y, path):
    write_gzip_list(y, path)
    assert read_gzip_list(path) == y
    os.remove(path)


def test_write_read_gzip_json_list(y, path):
    write_gzip_json_list(y, path)
    assert read_gzip_json_list(path) == y
    os.remove(path)
