import json
from pathlib import Path
from typing import Callable, Dict, List, Union


def write_jsonl(
    x: List[dict],
    path: Union[str, Path],
    callback: Callable,
    encoding: str = "utf-8",
) -> None:
    with open(path, "w", encoding=encoding) as f:
        for y in x:
            y = callback(y) if callback is not None else y
            f.write(json.dumps(y) + "\n")


def read_jsonl(
    path: Union[str, Path],
    callback: Callable,
    generator: bool = False,
    encoding: str = "utf-8",
) -> List[Dict]:
    with open(path, "r", encoding=encoding) as f:
        if not generator:
            x = [json.loads(line) for line in f]
            if callback is not None:
                x = [callback(y) for y in x]
            return x
        else:
            for line in f:
                x = json.loads(line)
                yield callback(x) if callback is not None else x
