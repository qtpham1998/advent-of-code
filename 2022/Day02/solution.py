from enum import Enum

import utils

play_map = {'A': 0, 'B': 1, 'C': 2,  # Opponent
            'X': 0, 'Y': 1, 'Z': 2}  # Player

# Rock, Paper, Scissors (Player)
score_matrix = [[4, 8, 3],  # Rock
                [1, 5, 9],  # Paper
                [7, 2, 6]]  # Scissors (Opponent)


# Part 1
def calculate_play_result(play: str) -> int:
    play = play.split(' ')
    opponent = play_map[play[0]]
    player = play_map[play[1]]
    return score_matrix[opponent][player]


# Part 2
def calculate_move_result(play: str) -> int:
    play = play.split(' ')
    opponent = play_map[play[0]]
    result = play[1]
    if result == 'X':  # Loss
        return min(score_matrix[opponent])
    elif result == 'Y':  # Draw
        return score_matrix[opponent][opponent]
    else:  # Win
        return max(score_matrix[opponent])


if __name__ == "__main__":
    move_strat_result = utils.read_input_file(calculate_play_result)
    print("Part 1: Playing the indicated shapes, the total final score would be {}".format(sum(move_strat_result)))
    outcome_strat_result = utils.read_input_file(calculate_move_result)
    print("Part 2: Causing the indicated outcomes, the total final score would be {}".format(sum(outcome_strat_result)))
