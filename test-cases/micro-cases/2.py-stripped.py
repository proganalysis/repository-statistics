# Test using global variables as well as a parameter

x      = 5
y      = "s"


def func(x     )       :
    x += 1
    return x + y

z      = func("a")
