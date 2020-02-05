from typing import Any, Tuple, TypeVar
def det(a, b, c) -> Any: 
    return (b*b) - (4*a*c)

_T1 = TypeVar('_T1')
def step(a, b: _T1) -> Tuple[_T1, Any]:
    return (b, b+1)

def sum(f, n) -> Any:
    if n < 0:
        return 0
    return sum(f, n-1) + f*n

def loopy(x) -> Any:
    return loopy(x)

def isEven(n) -> Any:
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

