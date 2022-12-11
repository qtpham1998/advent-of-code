from typing import Callable, Union, List

import numpy as np


def read_input_file(func: Callable = None, use_list = False) -> Union[list, np.ndarray]:
    with open('./input.txt', 'r') as file:
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


def int_list(lst: str, sep: str = None) -> np.ndarray:
    return np.array(lst.split(sep)).astype(int)
