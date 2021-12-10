from collections import Counter
from queue import Queue

import numpy as np
import utils


ROWS, COLS = 0, 0

def pre_process_data(line: str) -> np.ndarray:
    return np.array(list(line))


def get_data() -> np.ndarray:
    return utils.read_input_file(pre_process_data).astype(int)


def is_low_point(heatmap: np.ndarray, x: int, y: int) -> bool:
    rows, cols = heatmap.shape
    adjacent = []
    if x > 0:
        adjacent.append(heatmap[x - 1, y])
    if x < rows - 1:
        adjacent.append(heatmap[x + 1, y])
    if y > 0:
        adjacent.append(heatmap[x, y - 1])
    if y < cols - 1:
        adjacent.append(heatmap[x, y + 1])

    return (heatmap[x, y] < np.array(adjacent)).all()


def get_risk_level_sum(heatmap: np.ndarray) -> int:
    total = 0
    for x in range(len(heatmap)):
        for y in range(len(heatmap[0])):
            if is_low_point(heatmap, x, y):
                total += 1 + heatmap[x, y]
    return total


def map_out_basin(heatmap: np.ndarray, tag: int, start: tuple) -> None:
    stack = Queue()
    stack.put(start)
    rows, cols = heatmap.shape
    while not stack.empty():
        x, y = stack.get()
        if x > 0 and heatmap[x - 1, y] == 1:
            heatmap[x - 1, y] = tag
            stack.put((x - 1, y))
        if x < rows - 1 and heatmap[x + 1, y] == 1:
            heatmap[x + 1, y] = tag
            stack.put((x + 1, y))
        if y > 0 and heatmap[x, y - 1] == 1:
            heatmap[x, y - 1] = tag
            stack.put((x, y - 1))
        if y < cols - 1 and heatmap[x, y + 1] == 1:
            heatmap[x, y + 1] = tag
            stack.put((x, y + 1))


def get_basin_sizes_product(heatmap: np.ndarray) -> int:
    heatmap = (heatmap < 9).astype(int)
    tag = 2
    for x in range(len(heatmap)):
        for y in range(len(heatmap[0])):
            if heatmap[x, y] == 1:
                map_out_basin(heatmap, tag, (x, y))
                tag += 1

    sizes = Counter(heatmap.flatten())
    sizes.pop(0)  # Remove '9' counts
    return np.prod(np.sort(list(sizes.values()))[-3:])


def main():
    # level = get_risk_level_sum(get_data())
    # print("The sum of the risk levels of all low points is {}".format(level))
    prod = get_basin_sizes_product(get_data())
    print("The product of basin sizes is {}".format(prod))


if __name__ == '__main__':
    main()
