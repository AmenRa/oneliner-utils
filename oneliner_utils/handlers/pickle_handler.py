import pickle
from pathlib import Path
from typing import Any, Union

from .path_handler import create_path


def read_pickle(path: Union[str, Path]) -> Any:
    with open(path, "rb") as f:
        x = pickle.load(f)
    return x


def write_pickle(x, path: Union[str, Path]) -> None:
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "wb") as f:
        pickle.dump(x, f)
