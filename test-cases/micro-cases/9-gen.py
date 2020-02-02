# Testing dictionary with multiple types
from typing import Dict, Union
from typing import Type
x                                                = {"1": 1, 2: "2"}

x[5] = bool

def func() -> Union[int, str, Type[bool]]                         :
    z = x[2]
    return z
