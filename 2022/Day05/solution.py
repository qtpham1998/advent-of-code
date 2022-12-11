import copy
from collections import defaultdict, namedtuple
from queue import LifoQueue

import re

import numpy as np

import utils

# [S]                 [T] [Q]
# [L]             [B] [M] [P]     [T]
# [F]     [S]     [Z] [N] [S]     [R]
# [Z] [R] [N]     [R] [D] [F]     [V]
# [D] [Z] [H] [J] [W] [G] [W]     [G]
# [B] [M] [C] [F] [H] [Z] [N] [R] [L]
# [R] [B] [L] [C] [G] [J] [L] [Z] [C]
# [H] [T] [Z] [S] [P] [V] [G] [M] [M]
#  1   2   3   4   5   6   7   8   9
initial_arrangement = {
    1: ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'],
    2: ['T', 'B', 'M', 'Z', 'R'],
    3: ['Z', 'L', 'C', 'H', 'N', 'S'],
    4: ['S', 'C', 'F', 'J'],
    5: ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
    6: ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
    7: ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
    8: ['M', 'Z', 'R'],
    9: ['M', 'C', 'L', 'G', 'V', 'R', 'T'],
}


Instruction = namedtuple("Instruction", ["Amount", "From", "To"])


def process_instr(line: str) -> Instruction:
    match = re.findall("move (\d+) from (\d) to (\d)", line)[0]
    return Instruction(int(match[0]), int(match[1]), int(match[2]))


def create_stacks() -> dict[int, LifoQueue]:
    stacks = defaultdict(LifoQueue)
    for i, crates in initial_arrangement.items():
        for c in crates:
            stacks[i].put(c)
    return stacks


def rearrange_crates(instrs: np.ndarray, stacks: dict[int, LifoQueue]) -> dict[int, LifoQueue]:
    for instr in instrs:
        for _ in range(instr.Amount):
            stacks[instr.To].put(stacks[instr.From].get())
    return stacks


def rearrange_crates_cratemover(instrs: np.ndarray, stacks: dict[int, LifoQueue]) -> dict[int, LifoQueue]:
    for instr in instrs:
        crates = []
        for _ in range(instr.Amount):
            crates.append(stacks[instr.From].get())
        for c in np.flip(crates):
            stacks[instr.To].put(c)
    return stacks


def get_top_crates(stacks: dict[int, LifoQueue]) -> str:
    top_crates = ""
    for num in range(1, len(stacks) + 1):
        top_crates += stacks[num].get()
    return top_crates


if __name__ == "__main__":
    stacks = create_stacks()
    instructions = utils.read_input_file(process_instr, use_list=True)
    # rearranged_stacks = rearrange_crates(instructions, stacks)
    # print("Part 1: After rearranging, the top crates are: {}".format(get_top_crates(rearranged_stacks)))
    rearranged_stacks = rearrange_crates_cratemover(instructions, stacks)
    print("Part 2: After rearranging, the top crates are: {}".format(get_top_crates(rearranged_stacks)))
