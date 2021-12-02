from typing import Callable


def read_input_file(func: Callable = None) -> list:
    with open('./input.txt', 'r') as file:
        lines = file.readlines()
        if func is None:
            return map_list(lambda x: x.strip(), lines)
        else:
            return map_list(lambda x: func(x.strip()), lines)


def map_list(func: Callable, lst: list) -> list:
    return list(map(func, lst))
