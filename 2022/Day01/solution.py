import numpy as np

import utils


def get_elf_total_calories(calories_list: str) -> int:
    calories = utils.number_list(calories_list, '\n')
    return sum(calories)


def get_top_n_calories(n: int) -> np.ndarray:
    elves_list = utils.read_whole_file().split('\n\n')
    total_calories_list = utils.map_list(get_elf_total_calories, elves_list)
    return np.sort(total_calories_list)[-n:]


if __name__ == "__main__":
    top_calories = get_top_n_calories(3)
    total = sum(top_calories)
    print("Part 1: The highest total Calories is {}".format(top_calories[-1]))
    print("Part 2: The sum of top 3 highest total Calories is {}".format(total))
