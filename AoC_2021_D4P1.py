from inp import day4_1, day4_2
from timeit import Timer

def setupcards(data):
    # returns a list of lists for rows of the bingo card
    cards = []
    td = data.split("\n\n")
    for c in td:
        tcard = c.split("\n")
        tcard = [x.replace("  ", " ").split(" ") for x in tcard]
        for i in range(len(tcard)):
            if '' in tcard[i]:
                tcard[i].remove('')
        cards += [tcard]
    return cards

def caller(data):
    # returns bingo caller numbers
    return data.split(",")

def bingo(inpcards, inpnumbers):
    cards = setupcards(inpcards)
    c = caller(inpnumbers)
    for n in c:
        v = statemachine(n, cards)
        if v:
            c = 0
            for r in v[0]:
                c += sum([int(x) for x in r if x != 'x'])
            return c * int(n)

def statemachine(num, cards):
    # returns False or winning card
    vcards = []
    for i in range(len(cards)):
        cards[i] = cardupdate(num, cards[i])
        if containsvictory(cards[i]):
            vcards += [cards[i]]
    if len(vcards) > 0:
        return vcards
    else:
        return False

def cardupdate(num, card):
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == num:
                card[i][j] = 'x'
                return card
    else:
        return card

def containsvictory(card):
    # horizontal
    for i in range(len(card)):
        if card[i].count('x') == len(card[i]):
            return True
    # vertical
    if card[0].count('x') > 1:
        for j in range(len(card[0])):
            if card[0][j] == 'x':
                for i in range(1, len(card[0])):

                    if card[0][j] != card[i][j]:
                        break
                else:
                    return True


if __name__ == '__main__':
    t = Timer(lambda: bingo(day4_2, day4_1))
    print(t.timeit(number=1))
    print(bingo(day4_2, day4_1))
