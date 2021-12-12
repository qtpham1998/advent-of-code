from queue import Queue

import numpy as np
import utils


def pre_process_data(line: str) -> np.ndarray:
    return np.array(list(line))


def get_data() -> np.ndarray:
    return utils.read_input_file(pre_process_data).astype(int)


def run_step(octopuses: np.ndarray) -> int:
    rows, cols = octopuses.shape
    octopuses += 1
    flash = octopuses >= 10

    while flash.any():
        for x, y in np.argwhere(flash):
            octopuses[np.maximum(0, x - 1):np.minimum(rows, x + 2), np.maximum(0, y - 1):np.minimum(cols, y + 2)] += 1
            octopuses[x, y] = -100
        flash = octopuses >= 10

    octopuses[octopuses < 0] = 0
    return (octopuses == 0).sum()


def count_flashes_for_steps(octopuses: np.ndarray, steps: int) -> int:
    flash_total = 0
    for _ in range(steps):
        flash_total += run_step(octopuses)
    return flash_total


def find_complete_flash_step(octopuses: np.ndarray) -> int:
    step = 0
    while True:
        run_step(octopuses)
        step += 1
        if (octopuses == 0).all():
            return step


def main():
    steps = 100
    num_flashes = count_flashes_for_steps(get_data(), steps)
    print("The number of flashes after {} steps are {}".format(steps, num_flashes))

    step = find_complete_flash_step(get_data())
    print("The first step where all octopuses flash is {}".format(step))


if __name__ == '__main__':
    main()
