# http://www.codingdojo.org/cgi-bin/index.pl?KataPokerHands

from enum import Enum
RESULTS = Enum('RESULTS', 'WIN DRAW LOSE')
# WIN, DRAW, LOSE = range(3)


# Integration method
def highcards_compare(player1, player2):
    results = (compare(a, b) for a, b in reversed(list(zip(player1, player2))))
    return is_p1_win(results)

# Unit method


def is_p1_win(results):
    for i in results:
        result = i
        if result is not RESULTS.DRAW:
            break
    return result

# Integration method


def compare(a, b):
    score_a, score_b = (get_card_score(i) for i in [a, b])
    return versus(score_a, score_b)

# Unit method


def versus(score_a, score_b):
    # answer = LOSE
    answer = RESULTS.LOSE
    if score_a > score_b:
        # answer = WIN
        answer = RESULTS.WIN
    elif score_a == score_b:
        # answer = DRAW
        answer = RESULTS.DRAW
    return answer

# Unit method


def get_card_score(card):
    first_letter = card[0]
    score_table = [str(i) for i in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']
    return score_table.index(first_letter) + 2


def get_set_number_of_cards(cards):
    cards_number = [i[0] for i in cards]
    return len(set(cards_number))


def check_one_pair(cards):
    return get_set_number_of_cards(cards) == 4


def check_two_pair(cards):
    return get_set_number_of_cards(cards) == 3
