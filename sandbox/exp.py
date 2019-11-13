
from typing import List, Union, Tuple


def multi_list(l: List[str]):
    l.append(1)
    return l

def multi_list_add_one(l: List[Union[int, str]]):
    l.append(1)
    l.append(2)
    return l

def return_diff_type(l: List[Union[int, str]]) -> List[int]:
    l.append(1)
    return l
