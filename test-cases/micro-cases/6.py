# Testing class with invoking functions
from typing import Any
x: int = 1

class myClass:
    x: int
    y: str
    def __init__(self):
        self.x = 1
    def func(self):
        self.y = "s"
    def func1(self) -> str:
        return self.y


y: myClass = myClass()
y.func()
a: str = y.func1()

z: myClass = myClass()
b: Any = z.func1()
