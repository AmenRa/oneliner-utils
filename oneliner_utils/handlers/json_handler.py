import json
from pathlib import Path
from typing import Dict, Union


def write_json(
    x: Dict, path: Union[str, Path], encoding: str = "utf-8"
) -> None:
    with open(path, "w", encoding=encoding) as f:
        f.write(json.dumps(x, indent=4))


def read_json(path: Union[str, Path], encoding: str = "utf-8") -> Dict:
    with open(path, "r", encoding=encoding) as f:
        x = json.loads(f.read())
    return x
