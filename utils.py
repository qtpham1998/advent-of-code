from typing import Callable, Union, List

import numpy as np


def read_input_file(func: Callable = None) -> np.ndarray:
    with open('./input.txt', 'r') as file:
        lines = file.readlines()
        if func is None:
            return map_list(lambda x: x.strip(), lines)
        else:
            return map_list(lambda x: func(x.strip()), lines)


def map_list(func: Callable, lst: Union[List, np.ndarray]) -> np.ndarray:
    return np.array(list(map(func, lst)), dtype=object)
