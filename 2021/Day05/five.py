from collections import defaultdict
from typing import Union

import numpy as np
import utils


def pre_process_data(data: str) -> np.ndarray:
    points = data.split(' -> ')
    return utils.number_list(','.join(points), ',')


def get_data() -> np.ndarray:
    return utils.read_input_file(pre_process_data)


def get_slope(x1: int, y1: int, x2: int, y2: int) -> Union[int, None]:
    return None if x1 == x2 else (y2 - y1) // (x2 - x1)


def get_segment_points(x1: int, y1: int, x2: int, y2: int) -> np.ndarray:
    m = get_slope(x1, y1, x2, y2)
    if m is None:
        y_range = range(y1, y2 + 1) if y2 > y1 else range(y2, y1 + 1)
        points = [(x1, y) for y in y_range]
    else:
        points = []
        c = y1 - m * x1
        x_range = range(x1, x2 + 1) if x2 > x1 else range(x2, x1 + 1)
        for x in x_range:
            points.append((x, m * x + c))
    return np.array(points, dtype=object)


def mark_dangerous_area(segments: np.ndarray) -> defaultdict:
    diagram = defaultdict(lambda: 0)
    for x1, y1, x2, y2 in segments:
        # if x1 == x2 or y1 == y1  // Part 1
        for x, y in get_segment_points(x1, y1, x2, y2):
            diagram[x, y] += 1
    return diagram


def get_intersection_points(diagram: defaultdict) -> int:
    return (np.array(list(diagram.values())) > 1).sum()


def main():
    segments = get_data()
    diagram = mark_dangerous_area(segments)
    count = get_intersection_points(diagram)
    print("The number of points intersecting with intersections is {}.".format(count))


if __name__ == '__main__':
    main()
