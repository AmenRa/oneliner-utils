from pathlib import Path
from typing import Callable, List, Union

from .common import apply_callback
from .path_handler import create_path


def read_file_to_generator(
    path: Union[str, Path],
    callback: Callable = None,
    encoding: str = "utf-8",
):
    with open(path, "r", encoding=encoding) as f:
        for line in f:
            line = line.strip()
            yield callback(line) if callback is not None else line


def read_file_to_list(
    path: Union[str, Path],
    callback: Callable = None,
    encoding: str = "utf-8",
):
    with open(path, "r", encoding=encoding) as f:
        lines = f.read().splitlines()
        lines = [apply_callback(line, callback) for line in lines]
        return lines


def read_list(
    path: Union[str, Path],
    callback: Callable = None,
    generator: bool = False,
    encoding: str = "utf-8",
) -> List[str]:
    if generator:
        return read_file_to_generator(path, callback, encoding)
    else:
        return read_file_to_list(path, callback, encoding)


def write_list(
    x: List[str],
    path: Union[str, Path],
    callback: Callable = None,
    encoding: str = "utf-8",
) -> None:
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding=encoding) as f:
        for y in x:
            f.write(apply_callback(y, callback) + "\n")
