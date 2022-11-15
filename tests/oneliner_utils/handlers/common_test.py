import os

import pytest

from oneliner_utils.handlers.common import apply_callback


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return {"band": "black sabbath", "genre": "doom"}


# TESTS ========================================================================
def callback(d):
    d.pop("genre", None)
    return d


def test_apply_callback(x):
    y = apply_callback(x, callback)
    assert y == {"band": "black sabbath"}


def test_apply_callback_none(x):
    y = apply_callback(x, None)
    assert y == x
