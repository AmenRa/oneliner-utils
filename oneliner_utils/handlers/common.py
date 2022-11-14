from typing import Any, Callable


def apply_callback(x, callback: Callable = None) -> Any:
    return callback(x) if callback is not None else x
