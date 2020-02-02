# Testing simple class

class myClass:
    x: int
    y: str

    def __init__(self):
        self.x = 1
    def func(self):
        self.y = "s"
    def func1(self) -> str:
        return self.y
