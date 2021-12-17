from inp import day17 as data
from timeit import Timer

#
def setupdata(data) -> list:
    out = []
    d = data.replace("target area: x=", "")
    d = d.split(", y=")
    x = [int(x) for x in d[0].split("..")]
    y = [int(x) for x in d[1].split("..")]
    out.append((x[0], y[1]))
    out.append((x[1], y[0]))
    return out


def runner(bounds):
    maxvalid = []
    xf = xfactors(bounds)
    for x in range(xf[0], xf[1]+1):
        # the 2000 upper bound was a guess.  18 second execution time....
        for y in range(1,2000):
            m, b = nextpoint([x, y], bounds)
            if b:
                maxvalid.append(m)
    return max(maxvalid)


def nextpoint(cv, bounds) -> (int, bool):
    # cv is a list contianing x, y initial velocity, bounds is a list of bounding tuples
    maxy = 0
    cp = [0,0]
    while True:
        cp[0] += cv[0]
        if inbounds(cp, bounds):
            return maxy, True
        else:
            cp[1] += cv[1]
            if cp[1] > maxy:
                maxy = cp[1]
            if inbounds(cp, bounds):
                return maxy, True
        if cp[1] < bounds[1][1]:
            return 0, False
        else:
            # if cv[0] == 0 there is no change to cv[0]
            if cv[0] > 0:
                cv[0] -= 1
            elif cv[0] < 0:
                cv[0] += 1
            cv[1] -= 1


def xfactors(bounds) -> list:
    r = []
    xlower = bounds[0][0]
    xhigher = bounds[1][0]
    i = 1
    while True:
        nv = int((1 + i)/2 * i)
        if nv > xlower:
            r.append(i)
            break
        i += 1
    while True:
        nv = int((1 + i)/2 * i)
        if nv > xhigher:
            r.append(i-1)
            break
        i += 1
    return r




def inbounds(cp, bounds) -> bool:
    if cp[0] < bounds[0][0] or cp[0] > bounds[1][0]:
        return False
    if cp[1] > bounds[0][1] or cp[1] < bounds[1][1]:
        return False
    return True


if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(data)))
    print(t.timeit(number=1))
    print(runner(setupdata(data)))
