from pathlib import Path
from typing import Union

import lz4.frame


def read_lz4(path: str) -> dict:
    with lz4.frame.open(path, mode="rb") as f:
        x = lz4.frame.decompress(f.read())

    return x


def write_lz4(x, path: Union[str, Path]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with lz4.frame.open(path, mode="wb") as f:
        f.write(lz4.frame.compress(x, compression_level=16))
