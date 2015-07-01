# http://www.codewars.com/kata/vasya-clerk/python


def solve(l):
    '''if l[0] != 25:
        return False
    if len(l) >= 2 and l[1] == 100:
        return False
    if len(l) >= 3 and l[2] >= 50 and l[1] != 25:
        return False
    return True'''

    money = {}
    money['25'] = 0
    money['50'] = 0
    money['100'] = 0

    for i in l:
        if i == 50 and money['25'] >= 1:
            money['25'] -= 1
        elif i == 100 and money['25'] >= 1 and money['50'] >= 1:
            money['25'] -= 1
            money['50'] -= 1
        elif i != 25:
            return False
        money[str(i)] += 1
    return True
