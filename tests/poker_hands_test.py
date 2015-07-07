# http://www.codingdojo.org/cgi-bin/index.pl?KataPokerHands

import poker_hands as pk
import unittest


class PokerHandsTest(unittest.TestCase):
    pass


@unittest.skip('')
class CompareHighRankCardsTest(unittest.TestCase):

    def _helpper_assert(self, player1, player2, answer):
        result = pk.highcards_compare(player1, player2)
        self.assertEqual(result, answer)

    def test_same_player_should_be_draw(self):
        player1 = ["2H"] * 5
        answer = pk.DRAW
        self._helpper_assert(player1, player1, answer)

    def test_win_in_first_card_should_be_win(self):
        player1 = ["7H"] * 5
        player2 = ["2H"] * 5
        answer = pk.WIN
        self._helpper_assert(player1, player2, answer)

    def test_lose_in_first_card_should_be_lose(self):
        player1 = ["2H"] * 5
        player2 = ["3H"] * 5
        answer = pk.LOSE
        self._helpper_assert(player1, player2, answer)

    def test_lose_in_second_card_should_be_lose(self):
        player1 = ["2H"] * 4 + ["3H"]
        player2 = ["3H"] * 5
        answer = pk.LOSE
        self._helpper_assert(player1, player2, answer)

    def test_lose_in_third_card_should_be_lose(self):
        player1 = ["3H"] * 3 + ["AH"] * 2
        player2 = ["AH"] * 5
        answer = pk.LOSE
        self._helpper_assert(player1, player2, answer)


class CompareCardTest(unittest.TestCase):

    def decorator_stub(func):
        expected_score_table = {"3": 3, "7": 7, "A": 14}

        def inner(*args, **kwargs):
            old_get_score = pk.get_card_score
            try:
                pk.get_card_score = lambda x: expected_score_table[x[0]]
                func(*args, **kwargs)
            finally:
                pk.get_card_score = old_get_score

        return inner

    @decorator_stub
    def _helpper_assert(self, a, b, answer):
        result = pk.compare(a, b)
        self.assertEqual(result, answer)

    def test_give_3C_7D_should_be_lose(self):
        a, b = "3C", "7D"
        answer = pk.LOSE
        self._helpper_assert(a, b, answer)

    def test_give_7D_3C_should_be_win(self):
        a, b = "7D", "3C"
        answer = pk.WIN
        self._helpper_assert(a, b, answer)

    def test_give_AD_AC_should_be_draw(self):
        a, b = "AD", "AC"
        answer = pk.DRAW
        self._helpper_assert(a, b, answer)


@unittest.skip('')
class CardScoreTest(unittest.TestCase):

    def _helpper_assert(self, card, answer):
        result = pk.get_card_score(card)
        self.assertEqual(result, answer)

    def test_give_3C_should_be_3(self):
        card = "3C"
        answer = 3
        self._helpper_assert(card, answer)

    def test_give_4S_should_be_4(self):
        card = "4S"
        answer = 4
        self._helpper_assert(card, answer)

    def test_give_AS_should_be_14(self):
        card = "AS"
        answer = 14
        self._helpper_assert(card, answer)

    def test_give_KS_should_be_13(self):
        card = "KS"
        answer = 13
        self._helpper_assert(card, answer)

    def test_give_JS_should_be_11(self):
        card = "JS"
        answer = 11
        self._helpper_assert(card, answer)

    def test_give_QS_should_be_12(self):
        card = "QS"
        answer = 12
        self._helpper_assert(card, answer)

    def test_give_TS_should_be_10(self):
        card = "TS"
        answer = 10
        self._helpper_assert(card, answer)
