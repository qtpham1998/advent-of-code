from collections import defaultdict

import numpy as np
import utils


def pre_process_data(line: str) -> tuple:
    return tuple(line.split('-'))


def get_data() -> defaultdict:
    data = utils.read_input_file(pre_process_data)
    return build_map(data)


def build_map(data: np.ndarray) -> defaultdict:
    cave_map = defaultdict(lambda: [])
    for c1, c2 in data:
        if c2 != 'start':
            cave_map[c1].append(c2)
        if c1 != 'start':
            cave_map[c2].append(c1)
    return cave_map


def cannot_visit_cave(cave: str, path: np.ndarray) -> bool:
    return cave.islower() and cave in path


def map_out_paths(curr_cave: str, path: np.ndarray, cave_map: defaultdict, visited_small_twice: bool) -> int:
    if curr_cave == "end":
        return 1

    if cannot_visit_cave(curr_cave, path):
        if visited_small_twice:  # Part 2
            return 0
        else:
            visited_small_twice = True

    path = np.append(path, curr_cave)
    num_paths = 0
    for next_cave in cave_map[curr_cave]:
        num_paths += map_out_paths(next_cave, path, cave_map, visited_small_twice)

    return num_paths


def get_possible_paths(cave_map: defaultdict) -> int:
    return map_out_paths('start', np.array([], dtype=str), cave_map, False)


def main():
    num_paths = get_possible_paths(get_data())
    print("The number of paths through the cave system is {}".format(num_paths))


if __name__ == '__main__':
    main()
