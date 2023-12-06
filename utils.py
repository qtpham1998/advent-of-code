import re
from typing import Callable, Union, List

import numpy as np


def read_input_file(func: Callable = None, use_list = False) -> Union[list, np.ndarray]:
    with open('./input.txt.txt', 'r') as file:
        lines = file.readlines()
        if func is None:
            return numpy_map_list(lambda x: x.strip(), lines)
        else:
            if use_list:
                return map_list(lambda x: func(x.strip()), lines)
            else:
                return numpy_map_list(lambda x: func(x.strip()), lines)


def read_whole_file(func: Callable = None):
    with open('./input.txt', 'r') as file:
        data = file.read().strip()
        if func is None:
            return data
        return func(data)


def numpy_map_list(func: Callable, lst: Union[List, np.ndarray]) -> np.ndarray:
    return np.array(list(map(func, lst)), dtype=object)


def map_list(func: Callable, lst: Union[List, np.ndarray]) -> list:
    return list(map(func, lst))


def number_list(lst: str, sep: str = "\\s+", num_type=int) -> np.ndarray:
    return np.array(re.split(sep, lst.strip())).astype(num_type)


def get_surrounding_area(inp_map: np.ndarray, x: int, y: int, x_len: int, y_len: int) -> np.ndarray:
    lb_x = max(0, x - 1)
    ub_x = min(len(inp_map), x + 1 + x_len)
    lb_y = max(0, y - 1)
    ub_y = min(len(inp_map[0]), y + 1 + y_len)
    return inp_map[lb_x:ub_x, lb_y: ub_y]
