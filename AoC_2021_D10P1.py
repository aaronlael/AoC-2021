from inp import day10
from timeit import Timer

reflect = {"(": ")",
           "[": "]",
           "{": "}",
           "<": ">"
           }
points = {")": 3,
          "]": 57,
          "}": 1197,
          ">": 25137
          }


def setupdata(data):
    return data.split("\n")


def caller(sdata):
    p = 0
    for line in sdata:
        p += corruption(line)
    return p


def corruption(line):
    closers = []
    openers = list(line)
    for i in range(len(openers)):
        if openers[i] in reflect:
            closers += [reflect[openers[i]]]
        else:
            if openers[i] != closers[-1]:
                return points[openers[i]]
            else:
                closers = closers[:-1]
    else:
        return 0


if __name__ == '__main__':
    t = Timer(lambda: caller(setupdata(day10)))
    print(t.timeit(number=1))
    print(caller(setupdata(day10)))
