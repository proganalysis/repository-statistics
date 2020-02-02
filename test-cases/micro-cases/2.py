# Test using global variables as well as a parameter

x: int = 5
y: str = "s"


def func(x: int) -> Any:
    x += 1
    return x + y

z: Any = func("a")
