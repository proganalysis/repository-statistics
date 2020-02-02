# Sample test from the pytype README
from typing import Any

def f() -> str       :
     return "PyCon"
def g() -> Any       :
     return f() + 2019
