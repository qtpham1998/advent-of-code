from queue import Queue

import numpy as np
import utils


def create_heightmap(line: str) -> np.ndarray:
    return np.array([*line])


def consider_step(start: tuple, dest: tuple, path: np.ndarray, heightmap: np.ndarray) -> bool:
    return heightmap[start] == 'S' or \
           (dest not in path and \
           ord(heightmap[dest]) - ord(heightmap[start]) <= 1)


def get_steps_to_consider(curr: tuple, max_x, max_y) -> list:
    steps = []
    x, y = curr
    if x > 0:
        steps.append((x - 1, y))
    if y > 0:
        steps.append((x, y - 1))
    if x < max_x - 1:
        steps.append((x + 1, y))
    if y < max_y - 1:
        steps.append((x, y + 1))
    return steps


def find_optimal_path_length(heightmap: np.ndarray) -> int:
    max_x, max_y = len(heightmap), len(heightmap[0])
    min_steps = max_x * max_y
    starting_point = tuple(np.argwhere(heightmap == 'S')[0])
    to_explore = Queue()
    to_explore.put([starting_point])
    while not to_explore.empty():
        path = to_explore.get()
        if len(path) >= min_steps:
            continue

        start = path[-1]
        for dest in get_steps_to_consider(start, max_x, max_y):
            if consider_step(start, dest, path, heightmap):
                new_path = path[:]
                new_path.append(dest)
                if heightmap[dest] == 'E':
                    min_steps = min(min_steps, len(new_path))
                else:
                    to_explore.put(new_path)

    return min_steps




if __name__ == "__main__":
    h_map = utils.read_input_file(create_heightmap)
    optimal_path = find_optimal_path_length(h_map)
