# http://www.codingdojo.org/cgi-bin/index.pl?KataPokerHands

from enum import Enum
RESULTS = Enum('RESULTS', 'WIN DRAW LOSE')
# WIN, DRAW, LOSE = range(3)


# Compare
def compare(a, b):

    def get_score(x):
        return ask_rank_score(ask_rank(x))

    result = RESULTS.LOSE
    score_a = get_score(a)
    score_b = get_score(b)

    if score_a > score_b:
        result = RESULTS.WIN
    elif score_a == score_b:
        result = RESULTS.DRAW
    return result


# Score
def ask_rank(cards):
    rule_ranks = [
        (is_straight_flush_rank, 'straight flush'),
        (check_four_of_kind, 'four of kind'),
        (check_full_house, 'full house'),
        (check_flush, 'flush'),
        (is_straight_rank, 'straight'),
        (check_three_of_kind, 'three of kind'),
        (check_two_pairs, 'two pairs'),
        (check_one_pair, 'pair'),
    ]

    result = 'high card'
    for rule, rank in rule_ranks:
        if rule(cards):
            result = rank
            break

    return result


def ask_rank_score(rank):
    rank_score = {
        'high card': 0,
        'pair': 1,
        'two pairs': 2,
        'three of kind': 3,
        'straight': 4,
        'flush': 5,
        'full house': 6,
        'four of kind': 7,
        'straight flush': 8
    }
    return rank_score.get(rank, 0)


# Integration method
def is_straight_rank(cards):
    return check_straight(cards) and not check_flush(cards)


def is_flush_rank(cards):
    return not check_straight(cards) and check_flush(cards)


def is_straight_flush_rank(cards):
    return check_straight(cards) and check_flush(cards)


# Unit method
def get_card_score(card):
    first_letter = card[0]
    score_table = [str(i) for i in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']
    return score_table.index(first_letter) + 2


def get_set_number_of_cards(cards):
    cards_number = [i[0] for i in cards]
    set_cards = set(cards_number)
    return [cards_number.count(i) for i in set_cards]


def check_one_pair(cards):
    return len(get_set_number_of_cards(cards)) == 4


def check_two_pairs(cards):
    count = sorted(get_set_number_of_cards(cards))
    return len(count) == 3 and count == [1, 2, 2]


def check_three_of_kind(cards):
    count = sorted(get_set_number_of_cards(cards))
    return len(count) == 3 and count == [1, 1, 3]


def check_straight(cards):
    sorted_cards = sorted([get_card_score(i) for i in cards])
    is_consecutive = sorted_cards[4] - sorted_cards[0] == 4
    is_distinct = len(set(sorted_cards)) == 5
    return is_consecutive and is_distinct


def check_flush(cards):
    set_suit_cards = {i[1] for i in cards}
    return len(set_suit_cards) == 1


def check_full_house(cards):
    count = sorted(get_set_number_of_cards(cards))
    return len(count) == 2 and count == [2, 3]


def check_four_of_kind(cards):
    count = sorted(get_set_number_of_cards(cards))
    return len(count) == 2 and count == [1, 4]
