import pickle
from pathlib import Path
from typing import Any, Union


def write_pickle(x, path: Union[str, Path]) -> None:
    with open(path, "wb") as f:
        pickle.dump(x, f)


def read_pickle(path: Union[str, Path]) -> Any:
    with open(path, "rb") as f:
        x = pickle.load(f)
    return x
