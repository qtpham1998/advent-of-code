import numpy as np
import utils


def count_increases(data: np.ndarray) -> int:
    count = 0
    for i in range(1, len(data)):
        count += data[i - 1] < data[i]
    return count


def count_increases_2(data: np.ndarray) -> int:
    count = 0
    for i in range(len(data) - 3):
        wndwA = np.sum(data[i: i+3])
        wndwB = np.sum(data[i+1: i+4])
        count += wndwA < wndwB
    return count


def main():
    data = utils.read_input_file().astype(int)
    count = count_increases_2(data)
    print("The number of increases is: {}".format(count))


if __name__ == '__main__':
    main()
