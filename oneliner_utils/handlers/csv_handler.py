import csv
import sys
from pathlib import Path
from typing import Callable, Dict, List, Union

from .common import apply_callback
from .path_handler import create_path


def read_csv_to_generator(
    path: Union[str, Path],
    delimiter=",",
    callback: Callable = None,
    encoding: str = "utf-8",
):
    with open(path, "r", encoding=encoding) as f:
        lines = csv.DictReader(f, skipinitialspace=True, delimiter=delimiter)
        for line in lines:
            yield apply_callback(line, callback)


def read_csv_to_list(
    path: Union[str, Path],
    delimiter=",",
    callback: Callable = None,
    encoding: str = "utf-8",
):
    with open(path, "r", encoding=encoding) as f:
        x = list(csv.DictReader(f, skipinitialspace=True, delimiter=delimiter))
    return [apply_callback(y, callback) for y in x]


def read_csv(
    path: Union[str, Path],
    callback: Callable = None,
    delimiter=",",
    generator: bool = False,
    encoding: str = "utf-8",
) -> List[Dict]:
    csv.field_size_limit(sys.maxsize)
    if generator:
        return read_csv_to_generator(path, delimiter, callback, encoding)
    else:
        return read_csv_to_list(path, delimiter, callback, encoding)


def write_csv(
    x: List[Dict],
    path: Union[str, Path],
    callback: Callable = None,
    delimiter: str = ",",
    encoding: str = "utf-8",
):
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding=encoding, newline="") as f:
        keys = list(x[0])
        dict_writer = csv.DictWriter(f, keys, delimiter=delimiter)
        dict_writer.writeheader()
        dict_writer.writerows([apply_callback(y, callback) for y in x])
