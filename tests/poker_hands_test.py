# http://www.codingdojo.org/cgi-bin/index.pl?KataPokerHands

import poker_hands as pk
import unittest


class PokerHandsTest(unittest.TestCase):
    pass


class CheckStraightTest(unittest.TestCase):

    def test_give_straight_flush_should_false(self):
        cards = ["TC", "JC", "QC", "KC", "AC"]
        answer = pk.check_straight(cards)
        self.assertEqual(False, answer)

    def test_give_10_J_Q_K_A_should_ture(self):
        cards = ["TC", "JD", "QH", "KC", "AH"]
        answer = pk.check_straight(cards)
        self.assertEqual(True, answer)

    def test_give_2_to_6_should_true(self):
        cards = ["2C", "3D", "4H", "5C", "6H"]
        answer = pk.check_straight(cards)
        self.assertEqual(True, answer)

    def test_give_7_to_3_should_true(self):
        cards = ["7C", "6C", "5H", "4C", "3H"]
        answer = pk.check_straight(cards)
        self.assertEqual(True, answer)

    def test_give_3_3_7_7_7_should_false(self):
        cards = ["3C", "3D", "7H", "7C", "7S"]
        answer = pk.check_straight(cards)
        self.assertEqual(False, answer)

    def test_give_3_7_7_7_7_should_false(self):
        cards = ["3C", "7D", "7H", "7C", "7S"]
        answer = pk.check_straight(cards)
        self.assertEqual(False, answer)

    def test_give_3_to_7_should_true(self):
        cards = ["3C", "4D", "5H", "6C", "7H"]
        answer = pk.check_straight(cards)
        self.assertEqual(True, answer)

    def test_give_2_to_5_and_7_should_false(self):
        cards = ["2C", "3D", "4H", "5C", "7H"]
        answer = pk.check_straight(cards)
        self.assertEqual(False, answer)


class CheckThreeOfKindTest(unittest.TestCase):

    def test_three_of_kind_should_true(self):
        cards = ["AC", "AD", "AH", "4C", "5H"]
        answer = pk.check_three_of_kind(cards)
        self.assertEqual(True, answer)

    def test_three_of_kind2_should_true(self):
        cards = ["AC", "AD", "4H", "AC", "5H"]
        answer = pk.check_three_of_kind(cards)
        self.assertEqual(True, answer)

    def test_three_of_kind3_should_true(self):
        cards = ["2C", "2D", "4H", "2C", "5H"]
        answer = pk.check_three_of_kind(cards)
        self.assertEqual(True, answer)

    def test_check_have_two_pair_should_false(self):
        cards = ["2H", "2D"] + ["3H", "3C", "4C"]
        answer = pk.check_three_of_kind(cards)
        self.assertEqual(False, answer)

    def test_give_full_house_should_false(self):
        cards = ["2H", "2D", "3C", "3C", "3S"]
        answer = pk.check_three_of_kind(cards)
        self.assertEqual(False, answer)

    def test_give_full_house2_should_false(self):
        cards = ["3C", "3C", "3S", "4H", "4D"]
        answer = pk.check_three_of_kind(cards)
        self.assertEqual(False, answer)


class CheckTwoPairCardsTest(unittest.TestCase):

    def test_check_have_two_pair_should_true(self):
        cards = ["2H", "2D"] + ["3H", "3C", "4C"]
        answer = pk.check_two_pair(cards)
        self.assertEqual(True, answer)

    def test_give_one_pair_should_false(self):
        cards = ["2H", "2D"] + ["7H", "3C", "4C"]
        answer = pk.check_two_pair(cards)
        self.assertEqual(False, answer)

    def test_check_have_two_pair2_should_true(self):
        cards = ["2H", "2D"] + ["3H", "4C", "3C"]
        answer = pk.check_two_pair(cards)
        self.assertEqual(True, answer)

    def test_give_four_of_kind_should_false(self):
        cards = ["2H", "2D", "2C", "2S", "3C"]
        answer = pk.check_two_pair(cards)
        self.assertEqual(False, answer)

    def test_give_full_house_should_false(self):
        cards = ["2H", "2D", "3C", "3C", "3S"]
        answer = pk.check_two_pair(cards)
        self.assertEqual(False, answer)

    def test_three_of_kind_should_false(self):
        cards = ["AC", "AD", "AH", "4C", "5H"]
        answer = pk.check_two_pair(cards)
        self.assertEqual(False, answer)


class CheckOnePairCardsTest(unittest.TestCase):

    def test_check_have_one_pair_should_true(self):
        cards = ["2H", "2D"] + ["AC", "3C", "4C"]
        answer = pk.check_one_pair(cards)
        self.assertEqual(True, answer)

    def test_check_have_one_pair2_should_true(self):
        cards = ["AH", "2D"] + ["2C", "3C", "4C"]
        answer = pk.check_one_pair(cards)
        self.assertEqual(True, answer)

    def test_check_dont_have_one_pair_should_false(self):
        cards = ["AC", "2C", "3C", "4C", "5H"]
        answer = pk.check_one_pair(cards)
        self.assertEqual(False, answer)

    def test_three_of_kind_should_false(self):
        cards = ["AC", "AD", "AH", "4C", "5H"]
        answer = pk.check_one_pair(cards)
        self.assertEqual(False, answer)

    def test_three_of_kind2_should_false(self):
        cards = ["AC", "AD", "4H", "AC", "5H"]
        answer = pk.check_one_pair(cards)
        self.assertEqual(False, answer)

    def test_check_have_two_should_false(self):
        cards = ["2H", "2D"] + ["AC", "AD", "2C"]
        answer = pk.check_one_pair(cards)
        self.assertEqual(False, answer)


class CompareHighRankCardsTest(unittest.TestCase):

    def _helpper_assert(self, player1, player2, answer):
        result = pk.highcards_compare(player1, player2)
        self.assertEqual(result, answer)

    def test_same_player_should_be_draw(self):
        player1 = ["2H"] * 5 + []
        answer = pk.RESULTS.DRAW
        self._helpper_assert(player1, player1, answer)

    def test_win_in_first_card_should_be_win(self):
        player1 = ["7H"] * 5
        player2 = ["2H"] * 5
        answer = pk.RESULTS.WIN
        self._helpper_assert(player1, player2, answer)

    def test_lose_in_first_card_should_be_lose(self):
        player1 = ["2H"] * 5
        player2 = ["3H"] * 5
        answer = pk.RESULTS.LOSE
        self._helpper_assert(player1, player2, answer)

    def test_lose_in_second_card_should_be_lose(self):
        player1 = ["2H"] * 4 + ["3H"]
        player2 = ["3H"] * 5
        answer = pk.RESULTS.LOSE
        self._helpper_assert(player1, player2, answer)

    def test_lose_in_third_card_should_be_lose(self):
        player1 = ["3H"] * 3 + ["AH"] * 2
        player2 = ["AH"] * 5
        answer = pk.RESULTS.LOSE
        self._helpper_assert(player1, player2, answer)


class IsP1WinTest(unittest.TestCase):

    def _helpper_assert(self, versus_results, answer):
        result = pk.is_p1_win(versus_results)
        self.assertEqual(result, answer)

    def test_all_draw_should_be_draw(self):
        versus_results = [pk.RESULTS.DRAW] * 5
        answer = pk.RESULTS.DRAW
        self._helpper_assert(versus_results, answer)

    def test_win_in_first_card_should_be_win(self):
        versus_results = [pk.RESULTS.WIN] + [pk.RESULTS.DRAW] * 4
        answer = pk.RESULTS.WIN
        self._helpper_assert(versus_results, answer)

    def test_lose_in_first_card_should_be_lose(self):
        versus_results = [pk.RESULTS.LOSE] + [pk.RESULTS.DRAW] * 4
        answer = pk.RESULTS.LOSE
        self._helpper_assert(versus_results, answer)

    def test_lose_in_second_card_should_be_lose(self):
        versus_results = [
            pk.RESULTS.DRAW, pk.RESULTS.LOSE] + [pk.RESULTS.DRAW] * 3
        answer = pk.RESULTS.LOSE
        self._helpper_assert(versus_results, answer)

    def test_lose_in_third_card_should_be_lose(self):
        versus_results = [pk.RESULTS.DRAW] * 2 + [pk.RESULTS.LOSE] * 3
        answer = pk.RESULTS.LOSE
        self._helpper_assert(versus_results, answer)


class CompareCardTest(unittest.TestCase):

    def _helpper_assert(self, a, b, answer):
        result = pk.compare(a, b)
        self.assertEqual(result, answer)

    def test_give_3C_7D_should_be_lose(self):
        a, b = "3C", "7D"
        answer = pk.RESULTS.LOSE
        self._helpper_assert(a, b, answer)

    def test_give_7D_3C_should_be_win(self):
        a, b = "7D", "3C"
        answer = pk.RESULTS.WIN
        self._helpper_assert(a, b, answer)

    def test_give_AD_AC_should_be_draw(self):
        a, b = "AD", "AC"
        answer = pk.RESULTS.DRAW
        self._helpper_assert(a, b, answer)


class VersusTest(unittest.TestCase):

    def _helpper_assert(self, a, b, answer):
        result = pk.versus(a, b)
        self.assertEqual(result, answer)

    def test_give_3_7_should_be_lose(self):
        a, b = 3, 7
        answer = pk.RESULTS.LOSE
        self._helpper_assert(a, b, answer)

    def test_give_7_3_should_be_win(self):
        a, b = 7, 3
        answer = pk.RESULTS.WIN
        self._helpper_assert(a, b, answer)

    def test_give_14_14_should_be_draw(self):
        a, b = 14, 14
        answer = pk.RESULTS.DRAW
        self._helpper_assert(a, b, answer)


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
