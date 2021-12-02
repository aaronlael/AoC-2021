from inp import day2
from timeit import Timer

def setupdata(data):
    return [x.split(" ") for x in data.split("\n")]

def position(sdata):
    pos = { 'x' : 0, 'y': 0 }
    for x in sdata:
        if x[0] == 'forward':
            pos['x'] += int(x[1])
        elif x[0] == 'down':
            pos['y'] += int(x[1])
        elif x[0] == 'up':
            pos['y'] -= int(x[1])
    return pos['x'] * pos['y']

if __name__ == '__main__':
    t = Timer(lambda: position(setupdata(day2)))
    print(t.timeit(number=1))
    print(position(setupdata(day2)))
