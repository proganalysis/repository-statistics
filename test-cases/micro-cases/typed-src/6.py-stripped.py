# Testing class with invoking functions
from typing import Any
x: int = 1

class myClass:
    #: int
    #: str
    x: int
    y: str
    def __init__(self) -> None:
        self.x = 1
    def func(self) -> None:
        self.y = "s"
    def func1(self) -> str       :
        return self.y


y: myClass = myClass()
y.func()
a: str = y.func1()

z: myClass = myClass()
b: Any = z.func1()
