# http://www.codewars.com/kata/vasya-clerk/python

import collections


def solve(l):
    # return normal(l)
    return ocp(l)


class Clerk_Factory():

    def create(self):
        rules = [
            Bill_25_Rule(),
            Bill_50_Change25_Rule(),
            Bill_100_Change25_3Times_Rule(),
            Bill_100_Change25_50_Rule()
        ]
        return Clerk(rules)


class Clerk():

    def __init__(cls, rules):
        cls.rules = rules

    def solve(self, l):
        cash = {25: 0, 50: 0, 100: 0}
        result = True

        for i in l:
            for rule in self.rules:
                if rule.is_handle(i, cash):
                    cash = rule.change(cash)
                    break
            else:
                result = False
                break
            cash[i] += 1

        return result


class Rule():

    def is_handle(self, x, cash):
        pass

    def change(self, cash):
        pass


class Bill_25_Rule(Rule):

    def is_handle(self, x, cash):
        return x == 25

    def change(self, cash):
        return cash


class Bill_50_Change25_Rule(Rule):

    def is_handle(self, x, cash):
        return x == 50 and cash[25] >= 1

    def change(self, cash):
        cash[25] -= 1
        return cash


class Bill_100_Change25_3Times_Rule(Rule):

    def is_handle(self, x, cash):
        return x == 100 and cash[25] >= 3

    def change(self, cash):
        cash[25] -= 3
        return cash


class Bill_100_Change25_50_Rule(Rule):

    def is_handle(self, x, cash):
        return x == 100 and cash[25] >= 1 and cash[50] >= 1

    def change(self, cash):
        cash[25] -= 1
        cash[50] -= 1
        return cash


def ocp(l):
    clerk = Clerk_Factory().create()
    return clerk.solve(l)


def normal(l):
    money = collections.defaultdict(int)
    result = True

    for i in l:
        if i == 50 and money['25'] >= 1:
            money['25'] -= 1
        elif i == 100:
            if money['25'] >= 1 and money['50'] >= 1:
                money['25'] -= 1
                money['50'] -= 1
            elif money['25'] >= 3:
                money['25'] -= 3
            else:
                result = False
        elif i != 25:
            result = False
            break

        money[str(i)] += 1
    return result
