from inp import day10
from timeit import Timer

reflect = {"(": ")",
           "[": "]",
           "{": "}",
           "<": ">"
           }
points = {")": 1,
          "]": 2,
          "}": 3,
          ">": 4
          }


def setupdata(data):
    return data.split("\n")


def caller(sdata):
    p = []
    for line in sdata:
        t = incomplete(line)
        if t > 0:
            p += [t]
    p.sort()
    return p[int(len(p)/2)]


def incomplete(line):
    closers = []
    openers = list(line)
    for i in range(len(openers)):
        if openers[i] in reflect:
            closers += [reflect[openers[i]]]
        else:
            if openers[i] != closers[-1]:
                return 0
            else:
                closers = closers[:-1]
    else:
        if len(closers) > 0:
            out = 0
            for c in closers[::-1]:
                out *= 5
                out += points[c]
            return out
        else:
            return 0


if __name__ == '__main__':
    t = Timer(lambda: caller(setupdata(day10)))
    print(t.timeit(number=1))
    print(caller(setupdata(day10)))
