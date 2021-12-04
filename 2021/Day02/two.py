import numpy as np
import utils


class Position:
    Depth = 0
    HPos = 0
    Aim = 0


def parse_commands(command: str) -> tuple:
    direction, units = command.split(' ')
    return direction, int(units)


def move_submarine(submarine: Position, direction: str, units: int):
    if direction.startswith('f'):
        submarine.HPos += units
    else:
        submarine.Depth += units if direction.startswith('d') else -units
        submarine.Aim += units if direction.startswith('d') else -units


def move_submarine_two(submarine: Position, direction: str, units: int):
    if direction.startswith('f'):
        submarine.HPos += units
        submarine.Depth += submarine.Aim * units
    else:
        submarine.Aim += units if direction.startswith('d') else -units


def get_final_destination(submarine: Position, commands: np.ndarray):
    for c, u in commands:
        move_submarine_two(submarine, c, u)


def main():
    submarine = Position()
    commands = utils.read_input_file(parse_commands)
    get_final_destination(submarine, commands)
    print("The final horizontal position by the final depth is: {}".format(submarine.HPos * submarine.Depth))


if __name__ == '__main__':
    main()