import gzip
from pathlib import Path
from typing import Any, Callable, List, Union


def read_gzip(path: Union[str, Path]) -> Any:
    with gzip.open(path, "rt") as f:
        x = f.read()
    return x


def read_gzip_list(
    path: Union[str, Path], callback: Callable, generator: bool = False
) -> List:
    with gzip.open(path, "rt") as f:
        if not generator:
            x = f.read().splitlines()
            if callback is not None:
                x = [callback(y) for y in x]
            return x
        else:
            for line in f:
                yield callback(line) if callback is not None else line
