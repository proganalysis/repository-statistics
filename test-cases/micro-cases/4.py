# Testing multi definition as well as scope and multi value return types
from typing import Tuple

x: int, y: int = 1, 2

def func(x: int) -> Tuple[str, int]:
    x = 1
    x += y
    x = "s"
    return x, y

def func2() -> int:
    return x + y
