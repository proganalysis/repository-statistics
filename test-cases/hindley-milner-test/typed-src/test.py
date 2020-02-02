from typing import TypeVar
_T0 = TypeVar('_T0')
def id(p: _T0) -> _T0:
  return p

def fun1(i: _T0) -> _T0:
    return id(i)

def fun(n: str) -> str:
  if id(True):
    return n+id("hi")
  else:
    return n

fun("hello")
fun1(1)
