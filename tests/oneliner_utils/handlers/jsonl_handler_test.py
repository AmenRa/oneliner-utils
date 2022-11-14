import os
import types

import pytest

from oneliner_utils import read_jsonl, write_jsonl


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return [
        {"band": "black sabbath", "genre": "doom"},
        {"band": "cannibal corpse", "genre": "death metal"},
    ]


@pytest.fixture
def path():
    return "tests.jsonl"


# TESTS ========================================================================
def test_write_read_jsonl(x, path):
    write_jsonl(x, path)
    assert read_jsonl(path) == x
    os.remove(path)


def test_write_read_jsonl_generator(x, path):
    write_jsonl(x, path)
    y = read_jsonl(path, generator=True)
    assert isinstance(y, types.GeneratorType)
    assert list(y) == x
    os.remove(path)
