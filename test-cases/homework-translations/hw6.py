def det(a, b, c): 
    return (b*b) - (4*a*c)

def step(a, b):
    return (b, b+1)

def sum(f, n):
    if n < 0:
        return 0
    return sum(f, n-1) + f*n

def loopy(x):
    return loopy(x)

def isEven(n):
    def even(n):
        if n == 0:
            return True
        else:
            return odd(n-1)
    def odd(n):
        if n == 0:
            return False
        else:
            return even(n-1)
    return even(n)

