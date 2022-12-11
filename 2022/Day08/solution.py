from queue import Queue

import numpy as np
import utils


def process_data(line: str) -> np.ndarray:
    return np.array(list(line)).astype(int)


def count_visible_trees(trees_map: np.ndarray[int]) -> np.ndarray:
    visibility_map = np.zeros_like(trees_map)
    x_len, y_len = trees_map.shape

    for x in range(x_len):
        for y in range(y_len):
            from_left = all(trees_map[x, : max(0, y)] < trees_map[x, y])
            from_right = all(trees_map[x, min(y_len, y + 1):] < trees_map[x, y])
            from_above = all(trees_map[: max(0, x), y] < trees_map[x, y])
            from_below = all(trees_map[min(x_len, x + 1):, y] < trees_map[x, y])
            visibility_map[x, y] = int(from_left or from_right or from_above or from_below)

    return sum(visibility_map.flatten())


def calculate_num_visible_trees(tree_line: np.ndarray) -> int:
    if tree_line.size == 0:
        return 0

    try:
        return list(tree_line).index(False) + 1
    except ValueError:
        return tree_line.size


def calculate_max_scenic_score(trees_map: np.ndarray[int]) -> np.ndarray:
    scenic_scores = np.zeros_like(trees_map)
    x_len, y_len = trees_map.shape

    for x in range(x_len):
        for y in range(y_len):
            from_left = calculate_num_visible_trees(np.flip(trees_map[x, : max(0, y)] < trees_map[x, y]))
            from_right = calculate_num_visible_trees(trees_map[x, min(y_len, y + 1):] < trees_map[x, y])
            from_above = calculate_num_visible_trees(np.flip(trees_map[: max(0, x), y] < trees_map[x, y]))
            from_below = calculate_num_visible_trees(trees_map[min(x_len, x + 1):, y] < trees_map[x, y])

            scenic_scores[x, y] = from_left * from_right * from_above * from_below

    return max(scenic_scores.flatten())


if __name__ == "__main__":
    trees = utils.read_input_file(process_data)
    visible_trees_count = count_visible_trees(trees)
    print("Part 1: The number of trees visible from outside is {}".format(visible_trees_count))
    max_scenic_score = calculate_max_scenic_score(trees)
    print("Part 2: The highest scenic score is {}".format(max_scenic_score))
