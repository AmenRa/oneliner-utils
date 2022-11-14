from pathlib import Path
from typing import Callable, Dict, List, Union

import orjson

from .common import apply_callback
from .path_handler import create_path


def read_jsonl_to_generator(path: Union[str, Path], callback: Callable = None):
    with open(path, "rb") as f:
        for line in f:
            line = orjson.loads(line)
            yield apply_callback(line, callback)


def read_jsonl_to_list(path: Union[str, Path], callback: Callable = None):
    with open(path, "rb") as f:
        lines = [orjson.loads(line) for line in f]
        return [apply_callback(line, callback) for line in lines]


def read_jsonl(
    path: Union[str, Path],
    callback: Callable = None,
    generator: bool = False,
) -> List[Dict]:
    if generator:
        return read_jsonl_to_generator(path, callback)
    else:
        return read_jsonl_to_list(path, callback)


def write_jsonl(
    x: List[dict],
    path: Union[str, Path],
    callback: Callable = None,
) -> None:
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "wb") as f:
        for y in x:
            f.write(orjson.dumps(apply_callback(y, callback)) + "\n".encode())
