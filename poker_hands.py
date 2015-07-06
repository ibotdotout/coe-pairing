# http://www.codingdojo.org/cgi-bin/index.pl?KataPokerHands


# enum
WIN, DRAW, LOSE = range(3)


def compare(a, b):
    answer = LOSE
    score_a, score_b = (get_card_score(i) for i in [a, b])
    if score_a > score_b:
        answer = WIN
    elif score_a == score_b:
        answer = DRAW
    return answer


def highcards_compare(player1, player2):
    for a, b in reversed(zip(player1, player2)):
        result = compare(a, b)
        if result is not DRAW:
            break
    return result


def get_card_score(card):
    first_letter = card[0]
    score_table = map(str, range(2, 10)) + ['T', 'J', 'Q', 'K', 'A']
    return score_table.index(first_letter) + 2
