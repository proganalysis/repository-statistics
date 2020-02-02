# Testing dictionary with multiple types
from typing import Dict, Union
x: Dict[Union[int, str], Union[int, bool, str]]  = {"1": 1, 2: "2"}

x[5] = bool

def func() -> Union[int, bool, str]:
    z = x[2]
    return z
