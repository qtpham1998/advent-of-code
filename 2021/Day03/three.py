from typing import Callable

import numpy as np
import utils


def to_array(line: str) -> np.ndarray:
    return np.array(list(line))


def get_most_common_bit(line: np.array) -> int:
    count = np.bincount(line)
    return 1 if count[0] == count[1] else np.argmax(count)


def get_least_common_bit(line: np.array) -> int:
    return 1 - get_most_common_bit(line)


def bin_arr_to_dec(arr: np.ndarray) -> int:
    binary = str.join('', arr.astype(str))
    return int(binary, 2)


def read_report(report: np.ndarray) -> (int, int):
    gamma_array = utils.map_list(get_most_common_bit, report)
    epsilon_array = 1 - gamma_array
    return bin_arr_to_dec(gamma_array), bin_arr_to_dec(epsilon_array)


def filter_list(lst: np.ndarray, indxs: np.ndarray, bit: int) -> np.ndarray:
    if len(lst) == 1:
        return lst
    filt = indxs == bit
    return lst[filt]


def process_list(data: np.ndarray, bit_search_f: Callable) -> int:
    data = data
    idx = 0

    while len(data) > 1 and idx < len(data[0]):
        bits_idx = data.transpose()[idx]
        bit = bit_search_f(bits_idx)
        data = filter_list(data, bits_idx, bit)
        idx += 1

    return bin_arr_to_dec(data[0])


def main():
    data = utils.read_input_file(to_array).transpose()
    gamma, epsilon = read_report(data)
    print("The gamma rate is {}, epsilon rate is {}. The power consumption is {}".format(gamma, epsilon,
                                                                                         gamma * epsilon))


def main_two():
    data = utils.read_input_file(to_array).astype(int)
    oxy_rating = process_list(data, get_most_common_bit)
    co2_rating = process_list(data, get_least_common_bit)
    print("The oxygen generator rating is {}, CO2 scrubber rating is {}. The life support rating is {}".format(
        oxy_rating, co2_rating, oxy_rating * co2_rating))


if __name__ == '__main__':
    main_two()


