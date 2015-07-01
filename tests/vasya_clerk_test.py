# http://www.codewars.com/kata/vasya-clerk/python

import unittest
import vasya_clerk


class VasyaClerkTest(unittest.TestCase):

    def _help_assert(self, l, ans):
        result = vasya_clerk.solve(l)
        self.assertEqual(result, ans)

    def test_give_25_should_be_true(self):
        l = [25]
        self._help_assert(l, True)

    def test_give_50_should_be_false(self):
        l = [50]
        self._help_assert(l, False)

    def test_give_100_should_be_false(self):
        l = [100]
        self._help_assert(l, False)

    def test_give_25_100_should_be_false(self):
        l = [25, 100]
        self._help_assert(l, False)

    def test_give_25_50_50_should_be_false(self):
        l = [25, 50, 50]
        self._help_assert(l, False)

    def test_give_25_50_100_should_be_false(self):
        l = [25, 50, 100]
        self._help_assert(l, False)

    def test_give_25_25_50_should_be_ture(self):
        l = [25, 25, 50]
        self._help_assert(l, True)

    def test_give_25_25_25_100_should_be_ture(self):
        l = [25, 25, 25, 100]
        self._help_assert(l, True)

    def test_give_25_100_50_should_be_false(self):
        l = [25, 100, 50]
        self._help_assert(l, False)

    def test_give_25_50_25_100_should_be_true(self):
        l = [25, 50, 25, 100]
        self._help_assert(l, True)
