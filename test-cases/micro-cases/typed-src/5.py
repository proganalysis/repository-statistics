# Testing simple class

class myClass:
    x: int
    y: str

    def __init__(self) -> None:
        self.x = 1
    def func(self) -> None:
        self.y = "s"
    def func1(self) -> str:
        return self.y
