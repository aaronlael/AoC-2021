from AoC_2021_D2P1 import setupdata
from inp import day2
from timeit import Timer


def aimposition(sdata):
    pos = { 'x' : 0, 'y': 0 }
    aim = 0
    for x in sdata:
        if x[0] == 'forward':
            pos['x'] += int(x[1])
            pos['y'] += int(x[1]) * aim
        elif x[0] == 'down':
            aim += int(x[1])
        elif x[0] == 'up':
            aim -= int(x[1])
    return pos['x'] * pos['y']


if __name__ == '__main__':
    t = Timer(lambda: aimposition(setupdata(day2)))
    print(t.timeit(number=1))
    print(aimposition(setupdata(day2)))
