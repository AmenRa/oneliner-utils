from pathlib import Path
from typing import Any, Union

import numpy as np

from .path_handler import create_path


def read_numpy(path: Union[str, Path]) -> np.ndarray:
    with open(path, "rb") as f:
        x = np.load(file=f)
    return x


def write_numpy(x: np.ndarray, path: Union[str, Path]) -> None:
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "wb") as f:
        np.save(file=f, arr=x)
