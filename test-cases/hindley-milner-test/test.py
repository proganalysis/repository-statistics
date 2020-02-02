def id(p):
  return p

def fun1(i):
    return id(i)

def fun(n: str):
  if id(True):
    return n+id("hi")
  else:
    return n

fun("hello")
fun1(1)
