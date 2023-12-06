import numpy as np
import utils


def get_data() -> np.ndarray:
    return utils.number_list(utils.read_whole_file(), ',')


def calculate_constant_fuel_cons(crab_positions: np.ndarray, position: int) -> int:
    return np.abs(crab_positions - position).sum()


def calculate_arith_series(num: int) -> float:
    return num / 2 * (num + 1)


def calculate_growing_fuel_cons(crab_positions: np.ndarray, position: int) -> int:
    consumption = np.abs(crab_positions - position)
    consumption = calculate_arith_series(consumption)
    return consumption.sum()


def get_minimum_fuel_spend(crab_positions: np.ndarray) -> int:
    max_position = crab_positions.max()
    fuel_spend = np.zeros((max_position,))
    for i in range(max_position):
        fuel_spend[i] = calculate_growing_fuel_cons(crab_positions, i)
    return fuel_spend.min()


def main():
    min_fuel_spend = get_minimum_fuel_spend(get_data())
    print("The minimum fuel to spend is {}".format(min_fuel_spend))


if __name__ == '__main__':
    main()
