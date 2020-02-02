# Testing list with multiple types
from typing import List, Union
x: List[Union[int, str]] = [1, 2, 3, 4]

def func1() -> int                   :
    return x[2]

def func2() -> Union[int, str]                   :
    x.append("s")
    return x[0]
