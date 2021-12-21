# from inp import day19 as data
from timeit import Timer
import itertools
import math
from d19_inp import day19 as data


def setupdata(data):
    # returns scanners in a list maintaing input order
    sdata = data.split("\n\n")
    sdata = [x.split("\n")[1:] for x in sdata]
    out = []
    for x in sdata:
        t = []
        for j in x:
            j = j.split(",")
            t.append((int(j[0]), int(j[1]), int(j[2])))
        out.append(t)
    return out


def runner(sdata):
    scanners = []
    for i in range(len(sdata)):
        scan = coords(sdata[i], i)
        scanners.append(scan)
    compscan = []
    compscan += scanners[0]["0"]
    scanners = scanners[1:]
    while len(scanners) > 0:
        offcoord, id = scannermatch(compscan, scanners)
        compscan = list(set(compscan + offcoord))
        scanners = [x for x in scanners if x["id"] != id]
    return len(compscan)

def scannermatch(top, scanners) -> list:
    for scanner in scanners:
        for i in range(24):
            for coord in scanner[str(i)]:
                for topcoord in top:
                    xoff = topcoord[0] - coord[0]
                    yoff = topcoord[1] - coord[1]
                    zoff = topcoord[2] - coord[2]
                    offcoord = [(x[0]+xoff, x[1]+yoff, x[2]+zoff) for x in scanner[str(i)]]
                    if len(set.intersection(set(top), set(offcoord))) >= 12:
                        print(scanner['id'])
                        return offcoord, scanner['id']


def coords(scanner, num) -> dict:
    d = {}
    for i in range(24):
        d[str(i)] = []
    d['id'] = num
    for coord in scanner:
        # credit u/PityUpvote on reddit - https://www.reddit.com/r/adventofcode/comments/rjwhdv/comment/hp65cya/?utm_source=share&utm_medium=web2x&context=3
        # positive x
        d["0"].append((+coord[0],+coord[1],+coord[2]))
        d["1"].append((+coord[0],-coord[2],+coord[1]))
        d["2"].append((+coord[0],-coord[1],-coord[2]))
        d["3"].append((+coord[0],+coord[2],-coord[1]))
        # negative x
        d["4"].append((-coord[0],-coord[1],+coord[2]))
        d["5"].append((-coord[0],+coord[2],+coord[1]))
        d["6"].append((-coord[0],+coord[1],-coord[2]))
        d["7"].append((-coord[0],-coord[2],-coord[1]))
        # positive y
        d["8"].append((+coord[1],+coord[2],+coord[0]))
        d["9"].append((+coord[1],-coord[0],+coord[2]))
        d["10"].append((+coord[1],-coord[2],-coord[0]))
        d["11"].append((+coord[1],+coord[0],-coord[2]))
        # negative y
        d["12"].append((-coord[1],-coord[2],+coord[0]))
        d["13"].append((-coord[1],+coord[0],+coord[2]))
        d["14"].append((-coord[1],+coord[2],-coord[0]))
        d["15"].append((-coord[1],-coord[0],-coord[2]))
        # positive z
        d["16"].append((+coord[2],+coord[0],+coord[1]))
        d["17"].append((+coord[2],-coord[1],+coord[0]))
        d["18"].append((+coord[2],-coord[0],-coord[1]))
        d["19"].append((+coord[2],+coord[1],-coord[0]))
        # negative z
        d["20"].append((-coord[2],-coord[0],+coord[1]))
        d["21"].append((-coord[2],+coord[1],+coord[0]))
        d["22"].append((-coord[2],+coord[0],-coord[1]))
        d["23"].append((-coord[2],-coord[1],-coord[0]))

    return d

if __name__ == '__main__':
    # t = Timer(lambda: runner(setupdata(data)))
    # print(t.timeit(number=1))
    print(runner(setupdata(data)))
