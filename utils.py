import re
from typing import Callable, Union, List

import numpy as np


def read_input_file(func: Callable = None, use_list=False) -> Union[list, np.ndarray]:
    """
    Reads input line by line and processes them if func is provided
    Args:
        func: Function to apply to each line
        use_list: Whether to return as a list instead of numpy array

    Returns: List of input lines
    """
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
    """
    Reads the input file as a whole, processes it if func is provided
    Args:
        func: Function to apply to input

    Returns: Input file content
    """
    with open('./input.txt', 'r') as file:
        data = file.read().strip()
        if func is None:
            return data
        return func(data)


def numpy_map_list(func: Callable, lst: Union[List, np.ndarray]) -> np.ndarray:
    """
    Applies a function to the list element wise and returns result as a numpy.array
    Args:
        func: Function to apply
        lst: List to apply function to

    Returns: Numpy array of results after applying function

    """
    return np.array(map_list(func, lst), dtype=object)


def map_list(func: Callable, lst: Union[List, np.ndarray]) -> list:
    """
    Applies a function to list element-wise
    Args:
        func: Function to apply
        lst: List to apply function to

    Returns: List of results after applying function
    """
    return list(map(func, lst))


def number_list(lst: str, sep: str = "\\s+", num_type=int) -> np.ndarray:
    """
    Converts string to array of numbers
    Args:
        lst: String containing the list of numbers
        sep: List separator, defaults to '\\s+'
        num_type: Number type, defaults to int.

    Returns: Numpy array of numbers
    """
    return np.array(re.split(sep, lst.strip())).astype(num_type)


def get_surrounding_area(inp_map: np.ndarray, x: int, y: int, x_len: int, y_len: int) -> np.ndarray:
    """
    Gets the surrounding area from a map
    Args:
        inp_map: Map
        x: Starting x coordinate
        y: Starting y coordinate
        x_len: Length of x-side
        y_len: Length of y-side

    Returns: The area surrounding the rectangle denoted by coordinates (x, y):(x + x_len, y + y_len).
    """
    lb_x = max(0, x - 1)
    ub_x = min(len(inp_map), x + 1 + x_len)
    lb_y = max(0, y - 1)
    ub_y = min(len(inp_map[0]), y + 1 + y_len)
    return inp_map[lb_x:ub_x, lb_y: ub_y]
