import numpy as np
import utils


def extrapolate_value(history: np.ndarray[int]) -> (int, int):
    if len(history) == 0 or np.all(history == 0):
        return 0, 0

    differences = []
    for i in range(1, len(history)):
        differences.append(history[i] - history[i - 1])

    prev_val, next_val = extrapolate_value(np.array(differences))
    return (history[0] - prev_val), (history[-1] + next_val)


def get_extrapolated_value(line: str) -> int:
    history = utils.number_list(line)
    return extrapolate_value(history)


if __name__ == '__main__':
    prev_vales, next_values = zip(*utils.read_input_file(get_extrapolated_value))
    print("Part 1: The sum of extrapolated values is {}".format(sum(next_values)))
    print("Part 2: The sum of extrapolated values is {}".format(sum(prev_vales)))
