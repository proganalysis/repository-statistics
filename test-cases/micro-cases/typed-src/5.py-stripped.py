# Testing simple class

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
