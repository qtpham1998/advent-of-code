import re

import numpy as np
import utils


def pre_process_data(line: str) -> np.ndarray:
    return np.array(list(line))


def extract_number(schematic: np.ndarray, x: int, y: int) -> (int, int):
    match = re.match("(\\d+)", ''.join(schematic[x, y:]))
    return int(match.group(1)), match.end(1)


def is_part_number(schematic: np.ndarray, x: int, y: int, number_len: int) -> bool:
    surrounding_area = utils.get_surrounding_area(schematic, x, y, x_len=1, y_len=number_len).flatten()
    match = re.search("[^.\\d]", ''.join(surrounding_area))
    return bool(match)


def find_part_numbers_total(schematic: np.ndarray) -> int:
    x, y, part_sum = 0, 0, 0
    y_len = len(schematic[0])
    while x < len(schematic):
        skip = 1

        if np.char.isdigit(schematic[x, y]):
            number, num_len = extract_number(schematic, x, y)
            skip = num_len
            if is_part_number(schematic, x, y, num_len):
                part_sum += number

        y += skip
        if y >= y_len:
            x += 1
            y = 0

    return part_sum


def update_gear_map(gear_map: np.ndarray, gear_ratio: np.ndarray, number_area: np.ndarray,
                    num_x: int, num_y: int, number:int) -> (np.ndarray, np.ndarray):
    for x_delta, y_delta in np.argwhere(number_area == "*"):
        gear_x = max(0, num_x - 1) + x_delta
        gear_y = max(0, num_y - 1) + y_delta
        gear_map[gear_x, gear_y] += 1
        gear_ratio[gear_x, gear_y] *= number
    return gear_map, gear_ratio


def build_gear_map(schematic: np.ndarray) -> np.ndarray:
    x, y = 0, 0
    gear_map = np.zeros(schematic.shape)
    gear_ratio = np.ones(schematic.shape)
    y_len = len(schematic[0])
    while x < len(schematic):
        skip = 1

        if np.char.isdigit(schematic[x, y]):
            number, num_len = extract_number(schematic, x, y)
            skip = num_len
            surrounding_area = utils.get_surrounding_area(schematic, x, y, 1, num_len)
            gear_map, gear_ratio = update_gear_map(gear_map, gear_ratio, surrounding_area, x, y, number)

        y += skip
        if y >= y_len:
            x += 1
            y = 0

    gear_ratio *= (gear_map == 2).astype(int)
    return gear_ratio


if __name__ == "__main__":
    schematic = utils.read_input_file(pre_process_data)
    part_numbers_sum = find_part_numbers_total(schematic)
    print("Part 1: The sum of part numbers is {}".format(part_numbers_sum))
    gear_ratio_sum = np.sum(build_gear_map(schematic))
    print("Part 2: The sum of gear ratios is {}".format(gear_ratio_sum))

