from inp import day4_1, day4_2
from timeit import Timer
from AoC_2021_D4P1 import setupcards, caller, statemachine, cardupdate, containsvictory

def bingo(inpcards, inpnumbers):
    cards = setupcards(inpcards)
    c = caller(inpnumbers)
    for n in c:
        v = statemachine(n, cards)
        if v:
            if len(cards) > 1:
                for ca in v:
                    cards.remove(ca)
            else:
                c = 0
                for r in v[0]:
                    c += sum([int(x) for x in r if x != 'x'])
                return c * int(n)
    else:
        return cards

if __name__ == '__main__':
    t = Timer(lambda: bingo(day4_2, day4_1))
    print(t.timeit(number=1))
    print(bingo(day4_2, day4_1))
