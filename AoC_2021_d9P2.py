from inp import day9
from timeit import Timer


def setupdata(data):
    t = [list(x) for x in data.split("\n")]
    v = []
    for i in t:
        v += [[int(x) for x in i]]
    return v


def runner(sdata):
    basins = []
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
                lows += [(x, y)]
    for v in lows:
        basins += [basincalc(v, sdata)]
    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


def basincalc(coord, sdata):
    coords = [coord]
    # left
    i = 0
    while True:
        # left
        if coords[i][0] - 1 >= 0:
            tc = sdata[coords[i][1]][coords[i][0] - 1]
            if tc != 9:
                tct = (coords[i][0] - 1, coords[i][1])
                if tct not in coords:
                    coords += [tct]
        # right
        if coords[i][0] + 1 < len(sdata[0]):
            tc = sdata[coords[i][1]][coords[i][0] + 1]
            if tc != 9:
                tct = (coords[i][0] + 1, coords[i][1])
                if tct not in coords:
                    coords += [tct]
        # down
        if coords[i][1] - 1 >= 0:
            tc = sdata[coords[i][1] - 1][coords[i][0]]
            if tc != 9:
                tct = (coords[i][0], coords[i][1] - 1)
                if tct not in coords:
                    coords += [tct]
        # up
        if coords[i][1] + 1 < len(sdata):
            tc = sdata[coords[i][1] + 1][coords[i][0]]
            if tc != 9:
                tct = (coords[i][0], coords[i][1] + 1)
                if tct not in coords:
                    coords += [tct]
        i += 1
        if i == len(coords):
            return len(coords)


if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(day9)))
    print(t.timeit(number=1))
    print(runner(setupdata(day9)))
