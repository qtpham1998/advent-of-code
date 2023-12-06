import re
import utils
from collections import deque

text_to_digit = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"
}


def parse_calibration_value(line: str) -> int:
    digits = deque()
    for c in line:
        if c.isdigit():
            digits.append(c)
    first_digit = digits.popleft() if digits else "0"
    last_digit = digits.pop() if digits else first_digit
    return int(first_digit + last_digit)


def to_digit(number: str) -> str:
    return number if number.isdigit() else text_to_digit[number]


def parse_calibration_value_regex(line: str) -> int:
    pattern = '(?=(one|two|three|four|five|six|seven|eight|nine|zero|\\d))'
    matches = re.findall(pattern, line)
    first_digit = to_digit(matches[0])
    last_digit = to_digit(matches[-1])
    return int(first_digit + last_digit)


if __name__ == "__main__":
    total = sum(utils.read_input_file(parse_calibration_value))
    print("Part 1: The calibration values sum is {}".format(total))
    total2 = sum(utils.read_input_file(parse_calibration_value_regex))
    print("Part 2: The calibration values sum is {}".format(total2))
