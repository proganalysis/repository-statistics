# Testing class with invoking functions
from typing import Any
x      = 1

class myClass:
    #: int
    #: str
    def __init__(self) -> None:
        self.x = 1
    def func(self) -> None:
        self.y = "s"
    def func1(self) -> str       :
        return self.y


y          = myClass()
y.func()
a      = y.func1()

z          = myClass()
b      = z.func1()
