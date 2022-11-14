from pathlib import Path
from typing import Dict, Union

import orjson

from .path_handler import create_path


def read_json(path: Union[str, Path]) -> Dict:
    with open(path, "rb") as f:
        x = orjson.loads(f.read())
    return x


def write_json(x: Dict, path: Union[str, Path]) -> None:
    path = create_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "wb") as f:
        f.write(orjson.dumps(x, option=orjson.OPT_INDENT_2))
