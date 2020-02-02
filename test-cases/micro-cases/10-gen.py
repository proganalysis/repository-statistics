from typing import Any
# Testing how precise parameters can be as well as return value

def func1(x     ) -> Any       :
    x += 1
    return x

def func2(y     ) -> Any       :
    z = func1(1) + y
    return z

a      = func2(2)
