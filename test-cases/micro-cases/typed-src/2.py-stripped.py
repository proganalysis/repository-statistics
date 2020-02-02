# Test using global variables as well as a parameter

from typing import Any
x: int = 5
y: str = "s"


def func(x     ) -> Any       :
    x += 1
    return x + y

z: Any = func("a")
