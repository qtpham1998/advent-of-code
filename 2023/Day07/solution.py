from collections import Counter
import utils

INC_JOKER = True


class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.char_count = Counter(cards)
        self.type_ranking = self.get_type_ranking()

    def get_type_ranking(self) -> int:
        """
        Assigns ranking for the hand type based on max value frequency and number of distinct values
        """
        char_count = dict(self.char_count)
        wildcards = 0
        if INC_JOKER and "J" in char_count:
            wildcards = char_count["J"]
            char_count.pop("J")
        max_freq = max(char_count.values(), default=0) + wildcards
        distinct_chars = max(len(char_count), 1)
        return max_freq - distinct_chars

    def compare_card_values(self, other):
        card_val_ordering = "J23456789TQKA" if INC_JOKER else "23456789TJQKA"
        other_ranks = list(map(card_val_ordering.index, other.cards))
        for i, c in enumerate(map(card_val_ordering.index, self.cards)):
            other_c = other_ranks[i]
            if c == other_c:
                continue
            else:
                return 1 if c > other_c else -1
        return 0

    def __lt__(self, other):
        return self.type_ranking < other.type_ranking or \
            (self.type_ranking == other.type_ranking and self.compare_card_values(other) == -1)


def process_data(line: str) -> Hand:
    hand, bid = line.split()
    return Hand(hand, int(bid))


def calculate_winnings(hands: list[Hand]) -> int:
    winnings = 0
    for r, hand in enumerate(sorted(hands)):
        winnings += (r + 1) * hand.bid
    return winnings


if __name__ == '__main__':
    hands = utils.read_input_file(process_data, use_list=True)
    total_winnings = calculate_winnings(hands)
    print("Part {}: The total winnings are {}".format(2 if INC_JOKER else 1, total_winnings))