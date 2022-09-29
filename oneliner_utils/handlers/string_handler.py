from pathlib import Path
from typing import Union


def write(x: str, path: Union[str, Path], encoding: str = "utf-8") -> None:
    with open(path, "w", encoding=encoding) as f:
        f.write(x)


def read(path: Union[str, Path], encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as f:
        x = f.read()
    return x
