# Testing multi definition as well as scope and multi value return types
from typing import Tuple

x              = 1, 2

def func(x     )                   :
    x = 1
    x += y
    x = "s"
    return x, y

def func2()       :
    return x + y
