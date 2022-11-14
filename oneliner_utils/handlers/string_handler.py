from pathlib import Path
from typing import Union

from .path_handler import create_path


def read(path: Union[str, Path], encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as f:
        x = f.read()
    return x


def write(x: str, path: Union[str, Path], encoding: str = "utf-8") -> None:
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding=encoding) as f:
        f.write(x)
