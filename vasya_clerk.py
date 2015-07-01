# http://www.codewars.com/kata/vasya-clerk/python

import collections


def solve(l):
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
