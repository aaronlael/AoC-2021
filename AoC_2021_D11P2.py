from inp import day11
from timeit import Timer


def setupdata(data):
    m = data.split("\n")
    out = []
    for r in m:
        out += [[int(x) for x in list(r)]]
    return out


def caller(sdata):
    i = 1
    while True:
        f, sdata = turn(sdata)
        if f == 100:
            return i
        else:
            i += 1


def turn(sdata):
    sdata = increment(sdata)
    b = True
    while b:
        flashed = False
        for y in range(len(sdata)):
            for x in range(len(sdata[0])):
                if sdata[y][x] == 0:
                    sdata = flash((x, y), sdata)
        for y in range(len(sdata)):
            for x in range(len(sdata[0])):
                if sdata[y][x] == 0:
                    flashed = True
        if not flashed:
            b = False
    return xcount(sdata)


def increment(sdata):
    for y in range(len(sdata)):
        for x in range(len(sdata[0])):
            if sdata[y][x] == 9:
                sdata[y][x] = 0
            else:
                sdata[y][x] += 1
    return sdata


def xcount(sdata):
    c = 0
    for y in range(len(sdata)):
        for x in range(len(sdata[0])):
            if sdata[y][x] == "X":
                c += 1
                sdata[y][x] = 0
    return c, sdata


def flash(coord, sdata):
    sdata[coord[1]][coord[0]] = "X"
    # Upper left
    if coord[0] - 1 >= 0 and coord[1] - 1 >= 0:
        y = coord[1] - 1
        x = coord[0] - 1
        if sdata[y][x] != "X" and sdata[y][x] != 0:
            if sdata[y][x] == 9:
                sdata[y][x] = 0
            else:
                sdata[y][x] += 1
    # left
    if coord[0] - 1 >= 0:
        y = coord[1]
        x = coord[0] - 1
        if sdata[y][x] != "X" and sdata[y][x] != 0:
            if sdata[y][x] == 9:
                sdata[y][x] = 0
            else:
                sdata[y][x] += 1
    # Down left
    if coord[0] - 1 >= 0 and coord[1] + 1 < 10:
        y = coord[1] + 1
        x = coord[0] - 1
        if sdata[y][x] != "X" and sdata[y][x] != 0:
            if sdata[y][x] == 9:
                sdata[y][x] = 0
            else:
                sdata[y][x] += 1
    # Down
    if coord[1] + 1 < 10:
        y = coord[1] + 1
        x = coord[0]
        if sdata[y][x] != "X" and sdata[y][x] != 0:
            if sdata[y][x] == 9:
                sdata[y][x] = 0
            else:
                sdata[y][x] += 1
    # Down Right
    if coord[0] + 1 < 10 and coord[1] + 1 < 10:
        y = coord[1] + 1
        x = coord[0] + 1
        if sdata[y][x] != "X" and sdata[y][x] != 0:
            if sdata[y][x] == 9:
                sdata[y][x] = 0
            else:
                sdata[y][x] += 1
    # Right
    if coord[0] + 1 < 10:
        y = coord[1]
        x = coord[0] + 1
        if sdata[y][x] != "X" and sdata[y][x] != 0:
            if sdata[y][x] == 9:
                sdata[y][x] = 0
            else:
                sdata[y][x] += 1
    # Upper right
    if coord[0] + 1 < 10 and coord[1] - 1 >= 0:
        y = coord[1] - 1
        x = coord[0] + 1
        if sdata[y][x] != "X" and sdata[y][x] != 0:
            if sdata[y][x] == 9:
                sdata[y][x] = 0
            else:
                sdata[y][x] += 1
    # Up
    if coord[1] - 1 >= 0:
        y = coord[1] - 1
        x = coord[0]
        if sdata[y][x] != "X" and sdata[y][x] != 0:
            if sdata[y][x] == 9:
                sdata[y][x] = 0
            else:
                sdata[y][x] += 1
    return sdata


if __name__ == '__main__':
    t = Timer(lambda: caller(setupdata(day11)))
    print(t.timeit(number=1))
    print(caller(setupdata(day11)))
