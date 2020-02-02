# Testing how precise parameters can be as well as return value

def func1(x     )       :
    x += 1
    return x

def func2(y     )       :
    z = func1(1) + y
    return z

a      = func2(2)
