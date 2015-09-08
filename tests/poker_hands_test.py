# http://www.codingdojo.org/cgi-bin/index.pl?KataPokerHands

import poker_hands as pk
import unittest


class PokerHandsTest(unittest.TestCase):

    def test_case_1_should_lose_high_card_ace(self):
        a = ["2H", "3D", "5S", "9C", "KD"]
        b = ["2C", "3H", "4S", "8C", "AH"]
        result = pk.poker_hands(a, b)
        self.assertEqual((pk.RESULTS.LOSE, "high card", 'Ace'), result)

    def test_case_2_should_win_full_house(self):
        a = ["2H", "4S", "4C", "2D", "4H"]
        b = ["2S", "8S", "AS", "QS", "3S"]
        result = pk.poker_hands(a, b)
        self.assertEqual((pk.RESULTS.WIN, "full house", None), result)

    def test_case_3_should_win_high_card_9(self):
        a = ["2H", "3D", "5S", "9C", "KD"]
        b = ["2C", "3H", "4S", "8C", "KH"]
        result = pk.poker_hands(a, b)
        self.assertEqual((pk.RESULTS.WIN, "high card", '9'), result)

    def test_case_4_shoud_tie(self):
        a = ["2H", "3D", "5S", "9C", "KD"]
        b = ["2D", "3H", "5C", "9S", "KH"]
        result = pk.poker_hands(a, b)
        self.assertEqual((pk.RESULTS.DRAW, None, None), result)


class CompareTest(unittest.TestCase):

    def test_give_full_house_vs_flush_should_win(self):
        a = ["2H", "4S", "4C", "2D", "4H"]
        b = ["2S", "8S", "AS", "QS", "3S"]
        result = pk.compare(a, b)
        self.assertEqual(pk.RESULTS.WIN, result)

    def test_give_same_rank_value_should_draw(self):
        a = ["2H", "4S", "4C", "2D", "4H"]
        b = ["2S", "4D", "4C", "2D", "4H"]
        result = pk.compare(a, b)
        self.assertEqual(pk.RESULTS.DRAW, result)

    def test_give_same_rank_not_same_value_should_lose(self):
        a = ["2H", "4S", "4C", "2D", "4H"]
        b = ["9S", "4D", "4C", "9D", "4H"]
        result = pk.compare(a, b)
        self.assertEqual(pk.RESULTS.LOSE, result)


class GetValueCardTest(unittest.TestCase):

    def test_give_9_9_9_A_2_should_9_14_2(self):
        a = ["9H", "9S", "9C", "AD", "2H"]
        result = pk.get_value_card(a)
        self.assertEqual([9, 14, 2], result)

    def test_give_9_9_A_A_2_should_14_9_2(self):
        a = ["9H", "9S", "AC", "AD", "2H"]
        result = pk.get_value_card(a)
        self.assertEqual([14, 9, 2], result)


class AskRankScoreTest(unittest.TestCase):

    def _helper_assert(self, rank, expected_answer):
        answer = pk.ask_rank_score(rank)
        self.assertEqual(expected_answer, answer)

    def test_give_high_card_should_be_0(self):
        rank = 'high card'
        self._helper_assert(rank, 0)

    def test_give_pair_should_be_1(self):
        rank = 'pair'
        self._helper_assert(rank, 1)

    def test_give_two_pairs_should_be_2(self):
        rank = 'two pairs'
        self._helper_assert(rank, 2)

    def test_give_three_of_kind_should_be_3(self):
        rank = 'three of kind'
        self._helper_assert(rank, 3)

    def test_give_straight_should_be_4(self):
        rank = 'straight'
        self._helper_assert(rank, 4)

    def test_give_flush_should_be_5(self):
        rank = 'flush'
        self._helper_assert(rank, 5)

    def test_give_full_house_should_be_6(self):
        rank = 'full house'
        self._helper_assert(rank, 6)

    def test_give_four_of_kind_should_be_7(self):
        rank = 'four of kind'
        self._helper_assert(rank, 7)

    def test_give_straight_flush_should_be_8(self):
        rank = 'straight flush'
        self._helper_assert(rank, 8)


class AskRankTest(unittest.TestCase):

    def test_give_T_T_T_A_A_shoud_be_full_house(self):
        cards = ["TC", "TD", "TH", "AC", "AH"]
        answer = pk.ask_rank(cards)
        self.assertEqual('full house', answer)

    def test_give_T_T_T_T_A_shoud_be_four_of_kind(self):
        cards = ["TC", "TD", "TH", "TS", "AH"]
        answer = pk.ask_rank(cards)
        self.assertEqual('four of kind', answer)

    def test_give_C_C_C_C_C_should_be_flush(self):
        cards = ["5C", "4C", "QC", "KC", "AC"]
        answer = pk.ask_rank(cards)
        self.assertEqual('flush', answer)

    def test_give_TC_JC_QC_KC_AC_should_be_straight_flush(self):
        cards = ["TC", "JC", "QC", "KC", "AC"]
        answer = pk.ask_rank(cards)
        self.assertEqual('straight flush', answer)

    def test_give_10_J_Q_K_A_should_straight(self):
        cards = ["TC", "JD", "QH", "KC", "AH"]
        answer = pk.ask_rank(cards)
        self.assertEqual('straight', answer)

    def test_give_T_T_T_2_A_shoud_be_three_of_kind(self):
        cards = ["TC", "TD", "TH", "2S", "AH"]
        answer = pk.ask_rank(cards)
        self.assertEqual('three of kind', answer)

    def test_give_2_2_3_4_3_should_be_two_pairs(self):
        cards = ["2H", "2D", "3H", "4C", "3C"]
        answer = pk.ask_rank(cards)
        self.assertEqual('two pairs', answer)

    def test_give_2_2_3_4_5_should_be_pair(self):
        cards = ["2H", "2D", "3H", "4C", "5C"]
        answer = pk.ask_rank(cards)
        self.assertEqual('pair', answer)

    def test_give_5_2_9_4_6_should_be_high_card(self):
        cards = ["5H", "2D", "9H", "4C", "6C"]
        answer = pk.ask_rank(cards)
        self.assertEqual('high card', answer)


class CheckFourOfKindTest(unittest.TestCase):

    def test_give_T_T_T_T_A_shoud_true(self):
        cards = ["TC", "TD", "TH", "TS", "AH"]
        answer = pk.check_four_of_kind(cards)
        self.assertEqual(True, answer)

    def test_give_full_house_should_false(self):
        cards = ["TC", "TD", "TH", "AC", "AH"]
        answer = pk.check_four_of_kind(cards)
        self.assertEqual(False, answer)


class CheckFullHouseTest(unittest.TestCase):

    def test_give_T_T_T_A_A_shoud_true(self):
        cards = ["TC", "TD", "TH", "AC", "AH"]
        answer = pk.check_full_house(cards)
        self.assertEqual(True, answer)

    def test_give_T_T_T_J_Q_should_false(self):
        cards = ["TC", "TD", "TH", "JC", "QH"]
        answer = pk.check_full_house(cards)
        self.assertEqual(False, answer)

    def test_give_A_T_T_T_A_shoud_true(self):
        cards = ["AC", "TD", "TH", "TC", "AH"]
        answer = pk.check_full_house(cards)
        self.assertEqual(True, answer)

    def test_give_three_of_kind_should_false(self):
        cards = ["AC", "AD", "4C", "5H", "AH"]
        answer = pk.check_full_house(cards)
        self.assertEqual(False, answer)

    def test_give_four_of_kind_shoud_false(self):
        cards = ["TC", "TD", "TH", "TS", "AH"]
        answer = pk.check_full_house(cards)
        self.assertEqual(False, answer)


class CheckStraightFlushTest(unittest.TestCase):

    def test_give_straight_flush_should_true(self):
        cards = ["TC", "JC", "QC", "KC", "AC"]
        answer = pk.is_straight_flush_rank(cards)
        self.assertEqual(True, answer)

    def test_give_flush_should_flash(self):
        cards = ["5C", "4C", "QC", "KC", "AC"]
        answer = pk.is_straight_flush_rank(cards)
        self.assertEqual(False, answer)

    def test_give_straight_should_flash(self):
        cards = ["TC", "JD", "QH", "KC", "AH"]
        answer = pk.is_straight_flush_rank(cards)
        self.assertEqual(False, answer)


class CheckFlushTest(unittest.TestCase):

    def test_give_C_C_C_C_C_should_true(self):
        cards = ["5C", "4C", "QC", "KC", "AC"]
        answer = pk.is_flush_rank(cards)
        self.assertEqual(True, answer)

    def test_give_D_D_D_D_D_should_true(self):
        cards = ["5D", "4D", "QD", "KD", "AD"]
        answer = pk.is_flush_rank(cards)
        self.assertEqual(True, answer)

    def test_give_H_H_H_H_H_should_true(self):
        cards = ["5H", "4H", "QH", "KH", "AH"]
        answer = pk.is_flush_rank(cards)
        self.assertEqual(True, answer)

    def test_give_S_S_S_S_S_should_true(self):
        cards = ["5S", "4S", "QS", "KS", "AS"]
        answer = pk.is_flush_rank(cards)
        self.assertEqual(True, answer)

    def test_give_C_C_C_C_H_should_false(self):
        cards = ["5C", "4C", "QC", "KC", "AH"]
        answer = pk.is_flush_rank(cards)
        self.assertEqual(False, answer)

    def test_give_C_C_D_C_D_should_false(self):
        cards = ["5C", "4C", "QD", "KC", "AD"]
        answer = pk.is_flush_rank(cards)
        self.assertEqual(False, answer)

    def test_give_straight_flush_should_false(self):
        cards = ["TC", "JC", "QC", "KC", "AC"]
        answer = pk.is_flush_rank(cards)
        self.assertEqual(False, answer)


class CheckStraightTest(unittest.TestCase):

    def test_give_straight_flush_should_false(self):
        cards = ["TC", "JC", "QC", "KC", "AC"]
        answer = pk.is_straight_rank(cards)
        self.assertEqual(False, answer)

    def test_give_10_J_Q_K_A_should_ture(self):
        cards = ["TC", "JD", "QH", "KC", "AH"]
        answer = pk.is_straight_rank(cards)
        self.assertEqual(True, answer)

    def test_give_2_to_6_should_true(self):
        cards = ["2C", "3D", "4H", "5C", "6H"]
        answer = pk.is_straight_rank(cards)
        self.assertEqual(True, answer)

    def test_give_7_to_3_should_true(self):
        cards = ["7C", "6C", "5H", "4C", "3H"]
        answer = pk.is_straight_rank(cards)
        self.assertEqual(True, answer)

    def test_give_3_3_7_7_7_should_false(self):
        cards = ["3C", "3D", "7H", "7C", "7S"]
        answer = pk.is_straight_rank(cards)
        self.assertEqual(False, answer)

    def test_give_3_7_7_7_7_should_false(self):
        cards = ["3C", "7D", "7H", "7C", "7S"]
        answer = pk.is_straight_rank(cards)
        self.assertEqual(False, answer)

    def test_give_3_to_7_should_true(self):
        cards = ["3C", "4D", "5H", "6C", "7H"]
        answer = pk.is_straight_rank(cards)
        self.assertEqual(True, answer)

    def test_give_2_to_5_and_7_should_false(self):
        cards = ["2C", "3D", "4H", "5C", "7H"]
        answer = pk.is_straight_rank(cards)
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
        answer = pk.check_two_pairs(cards)
        self.assertEqual(True, answer)

    def test_give_one_pair_should_false(self):
        cards = ["2H", "2D"] + ["7H", "3C", "4C"]
        answer = pk.check_two_pairs(cards)
        self.assertEqual(False, answer)

    def test_check_have_two_pair2_should_true(self):
        cards = ["2H", "2D"] + ["3H", "4C", "3C"]
        answer = pk.check_two_pairs(cards)
        self.assertEqual(True, answer)

    def test_give_four_of_kind_should_false(self):
        cards = ["2H", "2D", "2C", "2S", "3C"]
        answer = pk.check_two_pairs(cards)
        self.assertEqual(False, answer)

    def test_give_full_house_should_false(self):
        cards = ["2H", "2D", "3C", "3C", "3S"]
        answer = pk.check_two_pairs(cards)
        self.assertEqual(False, answer)

    def test_three_of_kind_should_false(self):
        cards = ["AC", "AD", "AH", "4C", "5H"]
        answer = pk.check_two_pairs(cards)
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
