import gzip
from pathlib import Path
from typing import Any, Callable, List, Union

import orjson

from .common import apply_callback
from .path_handler import create_path


# String -----------------------------------------------------------------------
def read_gzip(path: Union[str, Path]) -> Any:
    with gzip.open(path, "rt") as f:
        x = f.read()
    return x


def write_gzip(x: str, path: Union[str, Path]) -> Any:
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with gzip.open(path, "wt") as f:
        f.write(x)


# List of Strings --------------------------------------------------------------
def read_gzip_to_generator(path: Union[str, Path], callback: Callable = None):
    with gzip.open(path, "rt") as f:
        for line in f:
            line = line.strip()
            yield apply_callback(line, callback)


def read_gzip_to_list(path: Union[str, Path], callback: Callable = None):
    with gzip.open(path, "rt") as f:
        lines = f.read().splitlines()
        return [apply_callback(line, callback) for line in lines]


def read_gzip_list(
    path: Union[str, Path],
    callback: Callable = None,
    generator: bool = False,
) -> List:
    if generator:
        return read_gzip_to_generator(path, callback)
    else:
        return read_gzip_to_list(path, callback)


def write_gzip_list(
    x: List[str],
    path: Union[str, Path],
    callback: Callable = None,
) -> List:
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with gzip.open(path, "wt") as f:
        for y in x:
            f.write(apply_callback(y, callback) + "\n")


# List of Json -----------------------------------------------------------------
def read_gzip_to_json_generator(
    path: Union[str, Path], callback: Callable = None
):
    with gzip.open(path, "rb") as f:
        for line in f:
            line = orjson.loads(line)
            yield apply_callback(line, callback)


def read_gzip_to_json_list(path: Union[str, Path], callback: Callable = None):
    with gzip.open(path, "rb") as f:
        lines = [orjson.loads(line) for line in f]
        return [apply_callback(line, callback) for line in lines]


def read_gzip_json_list(
    path: Union[str, Path],
    callback: Callable = None,
    generator: bool = False,
) -> List:
    if generator:
        return read_gzip_to_json_generator(path, callback)
    else:
        return read_gzip_to_json_list(path, callback)


def write_gzip_json_list(
    x: List[str],
    path: Union[str, Path],
    callback: Callable = None,
) -> List:
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with gzip.open(path, "wb") as f:
        for y in x:
            f.write(orjson.dumps(apply_callback(y, callback)) + "\n".encode())
