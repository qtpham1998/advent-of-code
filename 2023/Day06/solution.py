import math

import numpy as np
import utils


def process_data(inp: str) -> ((int, int), (np.ndarray, np.ndarray)):
    times_line, distances_line = inp.split("\n")
    times_line = times_line.split(":")[1]
    distances_line = distances_line.split(":")[1]

    times = utils.number_list(times_line)
    distances = utils.number_list(distances_line)
    time = int(times_line.replace(" ", ""))
    distance = int(distances_line.replace(" ", ""))
    return (time, distance), zip(times, distances)


def get_number_solutions(time: int, dist: int) -> int:
    x = math.sqrt(time**2 - 4 * dist)
    lower_boundary = math.floor((time - x) / 2) + 1
    upper_boundary = math.ceil((time + x) / 2)
    return upper_boundary - lower_boundary


def get_solutions_product(time_to_dist_rec: (np.ndarray, np.ndarray)) -> int:
    product = 1
    for time, dist in time_to_dist_rec:
        product *= get_number_solutions(time, dist)
    return product


if __name__ == '__main__':
    (t, d), time_to_dist_record = utils.read_whole_file(process_data)
    product = get_solutions_product(time_to_dist_record)
    print("Part 1: The product of the number of ways to win is {}".format(product))
    big_race_sol = get_number_solutions(t, d)
    print("Part 2: The number of ways to win the big race is {}".format(big_race_sol))

