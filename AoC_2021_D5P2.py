from inp import day5

def setupdata(data):
    return data.split("\n")

def dictop(coords, d):
    # manages a dict of points and the number of occurences
    x,y = [str(x) for x in coords]
    if x not in d:
        d[x] = {}
    if y not in d[x]:
        d[x][y] = 0
    d[x][y] += 1
    return d

def overlapcalc(sdata):
    # main function call
    d = {}
    overlap = 0
    for x in sdata:
        d = linetopoints(x, d)
    for x in d:
        for y in d[x]:
            if d[x][y] > 1:
                overlap += 1
    return overlap

def linetopoints(line, d):
    c1, c2 = line.split(" -> ")
    c1x, c1y = [int(x) for x in c1.split(",")]
    c2x, c2y = [int(x) for x in c2.split(",")]
    # horizontal and vertical handling
    if c1x == c2x:
        if c1y > c2y:
            r = c1y - c2y
            for i in range(r + 1):
                d = dictop((c1x, c2y + i), d)
        else:
            r = c2y - c1y
            for i in range(r + 1):
                d = dictop((c1x, c1y + i), d)
    elif c1y == c2y:
        if c1x > c2x:
            r = c1x - c2x
            for i in range(r + 1):
                d = dictop((c2x + i, c1y), d)
        else:
            r = c2x - c1x
            for i in range(r + 1):
                d = dictop((c1x + i, c1y), d)
    # diagonal handling
    else:
        if c1x < c2x:
            if c1y < c2y:
                d = dictop((c1x, c1y), d)
                tempc = (c1x, c1y)
                while tempc != (c2x, c2y):
                    tempc = (tempc[0] + 1, tempc[1] + 1)
                    d = dictop(tempc, d)
            else:
                d = dictop((c1x, c1y), d)
                tempc = (c1x, c1y)
                while tempc != (c2x, c2y):
                    tempc = (tempc[0] + 1, tempc[1] - 1)
                    d = dictop(tempc, d)
        elif c1x > c2x:
            if c1y > c2y:
                d = dictop((c2x, c2y), d)
                tempc = (c2x, c2y)
                while tempc != (c1x, c1y):
                    tempc = (tempc[0] + 1, tempc[1] + 1)
                    d = dictop(tempc, d)
            else:
                d = dictop((c2x, c2y), d)
                tempc = (c2x, c2y)
                while tempc != (c1x, c1y):
                    tempc = (tempc[0] + 1, tempc[1] - 1)
                    d = dictop(tempc, d)
    return d

if __name__ == '__main__':
    print(overlapcalc(setupdata(day5)))
