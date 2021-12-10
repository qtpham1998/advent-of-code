from queue import LifoQueue
import numpy as np
import utils


LEGAL_PAIRS = {
    '(': ')', '[': ']', '{': '}', '<': '>'
}
ERROR_SCORE = {
    ')': 3, ']': 57, '}': 1197, '>': 25137
}
COMPLETION_SCORE = {
    '(': 1, '[': 2, '{': 3, '<': 4
}


def get_data() -> np.ndarray:
    return utils.read_input_file()


def get_syntax_err_score(chunk: str) -> int:
    stack = LifoQueue()
    for c in chunk:
        if c in LEGAL_PAIRS.keys():
            stack.put(c)
        else:
            last_open_c = stack.get()
            if LEGAL_PAIRS[last_open_c] != c:
                return ERROR_SCORE[c]
    return 0


def get_total_error_score(lines: np.ndarray) -> int:
    total = 0
    for l in lines:
        total += get_syntax_err_score(l)
    return total


def calculate_completion_score(stack) -> int:
    score = 0
    while not stack.empty():
        c = stack.get()
        score = score * 5 + COMPLETION_SCORE[c]
    return score


def get_completion_score(chunk: str) -> int:
    stack = LifoQueue()
    for c in chunk:
        if c in LEGAL_PAIRS.keys():
            stack.put(c)
        else:
            last_open_c = stack.get()
            if LEGAL_PAIRS[last_open_c] != c:
                return 0
    return calculate_completion_score(stack)


def get_middle_completion_score(lines: np.ndarray) -> int:
    scores = []
    for l in lines:
        score = get_completion_score(l)
        if score != 0:
            scores.append(score)
    scores = sorted(scores)
    return scores[(len(scores) // 2)]


def main():
    score = get_total_error_score(get_data())
    print("The total syntax error score is {}".format(score))
    score = get_middle_completion_score(get_data())
    print("The middle completion score is {}".format(score))


if __name__ == '__main__':
    main()
