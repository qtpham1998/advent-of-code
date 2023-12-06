from typing import Union

import numpy as np
import utils


class Board:
    def __init__(self, data: str):
        numbers = np.empty(shape=(0, 5))
        data = data.split('\n')
        for d in data:
            row = utils.number_list(d)
            numbers = np.append(numbers, [row], axis=0)
        self.numbers = numbers
        self.total = numbers.sum()

    def update_board(self, num: int):
        self.numbers[self.numbers == num] = -1

    def get_unmarked_sum(self):
        return self.numbers.sum() + (self.numbers == -1).sum()

    def has_won(self):
        return np.any(np.apply_along_axis(check_row, 0, self.numbers)) or np.any(np.apply_along_axis(check_row, 1,
                                                                                                     self.numbers))


def check_row(row: np.ndarray) -> bool:
    return (row == -1).all()


def pre_process_data(data: str) -> (np.ndarray, np.ndarray):
    data = data.split('\n\n')
    draws = utils.number_list(data[0], ',')
    boards = utils.map_list(Board, data[1:])
    return draws, boards


def get_winning_board(draws: np.ndarray, boards: np.ndarray) -> (int, Union[Board, None]):
    for draw in draws:
        for board in boards:
            board.update_board(draw)
            if board.has_won():
                return draw, board
    return -1, None


def get_losing_board(draws: np.ndarray, boards: np.ndarray) -> (int, Union[Board, None]):
    for draw in draws:
        to_remove = []
        for i, board in enumerate(boards):
            board.update_board(draw)
            if board.has_won():
                to_remove.append(i)

        if len(boards) == 1 and len(to_remove) > 0:
            return draw, boards[0]
        boards = np.delete(boards, to_remove)
    return -1, None


def main():
    draws, boards = utils.read_whole_file(pre_process_data)
    last_draw, board = get_losing_board(draws, boards)
    if board is None:
        print("Error: No board returned")
        return
    u_sum = board.get_unmarked_sum()
    print("The unmarked sum is {}. The marked sum is {}. The final score is {}.".format(u_sum, last_draw,
                                                                                        u_sum * last_draw))


if __name__ == '__main__':
    main()
