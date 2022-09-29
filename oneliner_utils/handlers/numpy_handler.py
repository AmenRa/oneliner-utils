from pathlib import Path
from typing import Any, Union

import numpy as np


def write_numpy(x: np.ndarray, path: Union[str, Path]) -> None:
    with open(path, "wb") as f:
        np.save(file=f, arr=x)


def read_numpy(path: Union[str, Path]) -> np.ndarray:
    with open(path, "rb") as f:
        x = np.load(file=f)
    return x
