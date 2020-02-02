# Simple function return testing the scope of a variable name
x: int = 1
y: str = "s"

def func() -> bool:
    x = True
    return x
