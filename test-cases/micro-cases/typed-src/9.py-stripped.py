# Testing dictionary with multiple types
from typing import Dict, Union
from typing import Dict, Type, Union
x: Dict[Union[int, str], Union[int, str, Type[bool]]] = {"1": 1, 2: "2"}

x[5] = bool

def func() -> Union[int, str, Type[bool]]                         :
    z = x[2]
    return z
