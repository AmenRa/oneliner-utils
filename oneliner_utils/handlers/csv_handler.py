import csv
import sys
from pathlib import Path
from typing import Callable, Dict, List, Union


def write_csv(
    x: List[Dict],
    path: Union[str, Path],
    callback: Callable,
    delimiter: str = ",",
    encoding: str = "utf-8",
):
    with open(path, "w", encoding=encoding, newline="") as f:
        keys = list(x[0])
        dict_writer = csv.DictWriter(f, keys, delimiter=delimiter)
        dict_writer.writeheader()
        dict_writer.writerows(
            [callback(y) if callback is not None else y for y in x]
        )


def read_csv(
    path: Union[str, Path],
    callback: Callable,
    delimiter=",",
    encoding: str = "utf-8",
) -> List[Dict]:
    csv.field_size_limit(sys.maxsize)
    with open(path, "r", encoding=encoding) as f:
        x = list(csv.DictReader(f, skipinitialspace=True, delimiter=delimiter))
    return [callback(y) if callback is not None else y for y in x]
