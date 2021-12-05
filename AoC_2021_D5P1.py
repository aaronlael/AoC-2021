from inp import day5

def setupdata(data):
    return data.split("\n")

def overlapcalc(sdata):
    overlap = 0
    points = []
    for x in sdata:
        if isvertorhoriz(x):
            points += linetopoints(x)
    setpoints = list(set(points))
    for p in setpoints:
        if points.count(p) > 1:
            overlap +=1
    return overlap


def isvertorhoriz(line):
    c1, c2 = line.split(" -> ")
    if c1.split(",")[0] == c2.split(",")[0] or c1.split(",")[1] == c2.split(",")[1]:
        return True
    else:
        return False

def linetopoints(line):
    out = []
    c1, c2 = line.split(" -> ")
    c1x, c1y = [int(x) for x in c1.split(",")]
    c2x, c2y = [int(x) for x in c2.split(",")]
    if c1x == c2x:
        if c1y > c2y:
            r = c1y - c2y
            for i in range(r + 1):
                out += [(c1x, c2y + i)]
        else:
            r = c2y - c1y
            for i in range(r + 1):
                out += [(c1x, c1y + i)]
    else:
        if c1x > c2x:
            r = c1x - c2x
            for i in range(r + 1):
                out += [(c2x + i, c1y)]
        else:
            r = c2x - c1x
            for i in range(r + 1):
                out += [(c1x + i, c1y)]
    return out


if __name__ == '__main__':
    print(overlapcalc(setupdata(day5)))
