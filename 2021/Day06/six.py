from collections import defaultdict

import numpy as np
import utils


def pre_process_data(data) -> defaultdict:
    lanternfish = defaultdict(lambda: 0)
    for f in utils.int_list(data, ','):
        lanternfish[f] += 1
    return lanternfish


def get_data() -> defaultdict:
    return utils.read_whole_file(pre_process_data)


def simulate(lanternfish: defaultdict, days: int) -> defaultdict:
    for _ in range(days):
        new_spawns = lanternfish[0]
        for f in range(8):
            lanternfish[f] = lanternfish[f + 1]
        lanternfish[6] += new_spawns  # Reset
        lanternfish[8] = new_spawns  # Newly spawned
    return lanternfish


def count_lanternfish(lanternfish: defaultdict) -> int:
    return np.array(list(lanternfish.values())).sum()


def main():
    num_days = 256
    lanternfish = simulate(get_data(), num_days)
    count = count_lanternfish(lanternfish)
    print("The number of lanternfish after {} days is {}".format(num_days, count))


if __name__ == '__main__':
    main()