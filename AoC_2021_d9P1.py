from inp import day9
from timeit import Timer


def setupdata(data):
    t = [list(x) for x in data.split("\n")]
    v = []
    for i in t:
        v += [[int(x) for x in i]]
    return v


def runner(sdata):
    lows = []
    for y in range(len(sdata)):
        for x in range(len(sdata[0])):
            v = []
            # left
            if x-1 >= 0:
                v += [sdata[y][x-1]]
            # right
            if x+1 < len(sdata[y]):
                v += [sdata[y][x+1]]
            # down
            if y-1 >= 0:
                v += [sdata[y-1][x]]
            # up
            if y+1 < len(sdata):
                v += [sdata[y+1][x]]
            v = sorted(v)
            if sdata[y][x] < v[0]:
                lows += [sdata[y][x]]
    out = 0
    for l in lows:
        out += l+1
    return out


if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(day9)))
    print(t.timeit(number=1))
    print(runner(setupdata(day9)))
