import numpy as np

import utils


def calculate_priority(item: str) -> int:
    unicode = ord(item)
    if unicode < 91:  # A-Z = [65-90]
        return unicode - 38
    else:  # a-z = [97-122]
        return unicode - 96


def get_common_item_priority(bags: list) -> int:
    common = set(bags[0])
    for b in bags[1:]:
        common = common.intersection(b)
    return calculate_priority(common.pop())


def get_rucksack_priority(items: str) -> int:
    middle = len(items) // 2
    comp_one, comp_two = items[:middle], items[middle:]
    return get_common_item_priority([comp_one, comp_two])


def get_group_badge_priority(rucksacks: np.ndarray) -> int:
    total = 0
    i = 0
    while i < len(rucksacks):
        total += get_common_item_priority([rucksacks[i], rucksacks[i+1], rucksacks[i+2]])
        i += 3
    return total


if __name__ == "__main__":
    comp_priorities_sum = sum(utils.read_input_file(get_rucksack_priority))
    print("Part 1: The sum of the priorities of items on both compartments of each rucksack is {}".format(comp_priorities_sum))
    group_priorities_sum = get_group_badge_priority(utils.read_input_file())
    print("Part 2: The sum of the priorities of the groups' badge items is {}".format(group_priorities_sum))
