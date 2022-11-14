import os
from pathlib import Path


def create_path(path: str) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    return path


def join_path(*args: str) -> str:
    return Path(os.path.join(*args))
