from typing import Tuple
import numpy as np

import utils

from collections import namedtuple

Elf = namedtuple('Elf', ['Lower', 'Upper'])


def get_elf_sections(elf: str) -> Elf:
    lower, upper = elf.split('-')
    return Elf(int(lower), int(upper))


def process_pair_assignment(assignment: str) -> tuple[Elf, Elf]:
    elf_one, elf_two = assignment.split(',')
    return get_elf_sections(elf_one), get_elf_sections(elf_two)


def is_contained(elf_one: Elf, elf_two: Elf) -> bool:
    return elf_one.Lower <= elf_two.Lower and elf_one.Upper >= elf_two.Upper or \
           elf_one.Lower >= elf_two.Lower and elf_one.Upper <= elf_two.Upper


def count_fully_contained_pairs(assignments: list[(Elf, Elf)]) -> int:
    count = 0
    for elf_one, elf_two in assignments:
        count += int(is_contained(elf_one, elf_two))
    return count


def is_overlapping(elf_one: Elf, elf_two: Elf) -> bool:
    return not (elf_one.Upper < elf_two.Lower or elf_one.Lower > elf_two.Upper)


def count_overlapping_pairs(assignments: list[(Elf, Elf)]) -> int:
    count = 0
    for elf_one, elf_two in assignments:
        count += int(is_overlapping(elf_one, elf_two))
    return count


if __name__ == "__main__":
    assignments_data = utils.read_input_file(process_pair_assignment, use_list=True)
    contained_assignments = count_fully_contained_pairs(assignments_data)
    print("Part 1: The number of fully contained assignment pairs is {}".format(contained_assignments))
    overlapping_pairs = count_overlapping_pairs(assignments_data)
    print("Part 2: The number of overlapping assignment pairs is {}".format(overlapping_pairs))