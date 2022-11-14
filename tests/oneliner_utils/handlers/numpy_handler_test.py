import os

import numpy as np
import pytest

from oneliner_utils import read_numpy, write_numpy


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return np.array([1, 2, 3, 4, 5])


@pytest.fixture
def path():
    return "tests.npy"


# TESTS ========================================================================
def test_write_read(x, path):
    write_numpy(x, path)
    assert np.array_equal(read_numpy(path), x)
    os.remove(path)
