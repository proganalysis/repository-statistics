# Testing multi definition as well as scope and multi value return types
from typing import Tuple
from typing import Any

x              = 1, 2

def func(x     ) -> Tuple[str, Any]                   :
    x = 1
    x += y
    x = "s"
    return x, y

def func2() -> tuple       :
    return x + y
