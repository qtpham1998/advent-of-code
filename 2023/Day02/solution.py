from typing import Tuple, Any

import re
import utils


def get_cubes_count(record: str) -> tuple[int, int, int]:
    red_matches = re.search("(\\d+) red", record)
    red_cubes = int(red_matches.group(1)) if red_matches else 0

    green_matches = re.search("(\\d+) green", record)
    green_cubes = int(green_matches.group(1)) if green_matches else 0

    blue_matches = re.search("(\\d+) blue", record)
    blue_cubes = int(blue_matches.group(1)) if blue_matches else 0

    return red_cubes, green_cubes, blue_cubes


def is_round_eligible(rnd: str) -> bool:
    red_cubes, green_cubes, blue_cubes = get_cubes_count(rnd)
    return red_cubes <= 12 and green_cubes <= 13 and blue_cubes <= 14


def is_game_eligible(record: str) -> int:
    game = re.match("Game (\\d+): (.+)", record)
    game_id = game.group(1)
    eligible = True
    for rnd in game.group(2).split(";"):
        eligible = eligible and is_round_eligible(rnd)
    return int(game_id) if eligible else 0


def get_fewest_cubes(record: str) -> tuple[int, int, int]:
    min_red = 0
    min_green = 0
    min_blue = 0
    for rnd in record.split(";"):
        r, g, b = get_cubes_count(rnd)
        min_red = max(min_red, r)
        min_green = max(min_green, g)
        min_blue = max(min_blue, b)
    return min_red, min_green, min_blue


def get_cube_power(record: str) -> int:
    record = record.split(":")[1]
    (red, green, blue) = get_fewest_cubes(record)
    return red * green * blue


if __name__ == "__main__":
    eligible_games = sum(utils.read_input_file(is_game_eligible))
    print("The sum of eligible game IDs is {}".format(eligible_games))
    cube_power_sum = sum(utils.read_input_file(get_cube_power))
    print("The sum of cube set powers is {}".format(cube_power_sum))

