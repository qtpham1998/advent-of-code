from collections import defaultdict

import utils


def get_next_knot_new_position(curr_knot: tuple, next_knot: tuple) -> tuple:
    x_diff = curr_knot[0] - next_knot[0]
    y_diff = curr_knot[1] - next_knot[1]

    if abs(x_diff) < 2 and abs(y_diff) < 2:
        return next_knot

    x_delta = 0 if x_diff == 0 else x_diff / abs(x_diff)
    y_delta = 0 if y_diff == 0 else y_diff / abs(y_diff)
    return next_knot[0] + x_delta, next_knot[1] + y_delta


def calculate_tail_visited_pos(movements: list[tuple], knots_num=2) -> int:
    knots = []
    head_pos = (0, 0)
    tail_pos = (0, 0)
    for _ in range(knots_num - 2):
        knots.append((0, 0))
    knots.append(tail_pos)

    tail_visited = {(0, 0)}
    for direction, num in movements:
        if direction == 'U':
            x_delta = 0
            y_delta = 1
        elif direction == 'R':
            x_delta = 1
            y_delta = 0
        elif direction == 'L':
            x_delta = -1
            y_delta = 0
        else:
            x_delta = 0
            y_delta = -1

        for _ in range(num):
            head_pos = (head_pos[0] + x_delta, head_pos[1] + y_delta)
            curr_knot = head_pos
            for i in range(knots_num - 1):
                knots[i] = get_next_knot_new_position(curr_knot, knots[i])
                curr_knot = knots[i]
            tail_visited.add(knots[-1])

    return len(tail_visited)


def process_data(line: str) -> tuple:
    direction, num = line.split(' ')
    return direction, int(num)


if __name__ == "__main__":
    moves = utils.read_input_file(process_data)
    visited = calculate_tail_visited_pos(moves)
    print("Part 1: The tail of the rope visited {} positions.".format(visited))
    long_visited = calculate_tail_visited_pos(moves, 10)
    print("Part 2: The tail of the rope visited {} positions.".format(long_visited))
