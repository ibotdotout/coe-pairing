# http://www.codingdojo.org/cgi-bin/index.pl?KataPokerHands


def get_card_score(card):
    first_letter = card[0]
    score_table = map(str, range(2, 10)) + ['T', 'J', 'Q', 'K', 'A']
    return score_table.index(first_letter) + 2
