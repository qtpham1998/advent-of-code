from queue import Queue
import re
import numpy as np
import utils


def parse_card_inp(card: str) -> (int, int):
    card_id = int(re.match("Card\\s+(\\d+)", card).group(1))
    numbers = card.split(":")[1].split("|")
    winning_hand = set(utils.number_list(numbers[0].strip()))
    hand = set(utils.number_list(numbers[1].strip()))
    return card_id, len(winning_hand.intersection(hand))


def calculate_card_points(card: str) -> int:
    _, winning_nums_power = parse_card_inp(card)
    return np.floor(2 ** (winning_nums_power - 1))


def build_card_map(cards: list[str]) -> dict[int, range]:
    card_map = dict()
    for card in cards:
        card_id, count = parse_card_inp(card)
        card_map[card_id] = range(card_id + 1, card_id + count + 1)
    return card_map


def count_cards(card_map: dict[int, range]) -> int:
    card_count = {card: 1 for card in card_map.keys()}

    for curr_card in card_map.keys():
        for next_card in card_map[curr_card]:
            card_count[next_card] += card_count[curr_card]

    return sum(card_count.values())


if __name__ == "__main__":
    points = sum(utils.read_input_file(calculate_card_points))
    print("Part 1: The total points is {}".format(points))
    cards_map = build_card_map(utils.read_input_file())
    remaining_cards = count_cards(cards_map)
    print("Part 2: The number of remaining cards is {}".format(remaining_cards))

