from pathlib import Path
from typing import Callable, Dict, List, Union


def write_list(
    x: List[str],
    path: Union[str, Path],
    callback: Callable,
    encoding: str = "utf-8",
) -> None:
    with open(path, "w", encoding=encoding) as f:
        for y in x:
            y = callback(y) if callback is not None else y
            f.write(y + "\n")


def read_list(
    path: Union[str, Path],
    callback: Callable,
    generator: bool = False,
    encoding: str = "utf-8",
) -> List[str]:
    with open(path, "r", encoding=encoding) as f:
        if not generator:
            x = f.read().splitlines()
            if callback is not None:
                x = [callback(y) for y in x]
            return x
        else:
            for line in f:
                yield callback(line) if callback is not None else line
