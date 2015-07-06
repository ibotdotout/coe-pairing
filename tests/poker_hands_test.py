# http://www.codingdojo.org/cgi-bin/index.pl?KataPokerHands

import poker_hands as pk
import unittest


class PokerHandsTest(unittest.TestCase):
    pass


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
