# Testing how precise parameters can be as well as return value

def func1(x: int) -> int:
    x += 1
    return x

def func2(y: int) -> int:
    z = func1(1) + y
    return z

a: int = func2(2)
