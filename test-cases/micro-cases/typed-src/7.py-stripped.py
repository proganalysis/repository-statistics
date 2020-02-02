# Testing casting functions

def func1(y) -> int       :
    x = int(y)
    return x

def func2() -> int       :
    return 1 + func1("1")

