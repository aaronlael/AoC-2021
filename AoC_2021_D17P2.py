from inp import day17 as data
from timeit import Timer

# data = "target area: x=20..30, y=-10..-5"

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
    vc = 0
    coords = []
    xf = xfactors(bounds)
    # for x in range(xf[0], xf[1]+1):
    for x in range(xf[0],xf[1] ):
        yf = yfactors(bounds)
        # for y in range(yf[0], yf[1]+1):
        for y in range(yf[0],yf[1]):
            b, c = nextpoint([x, y], bounds)
            if b:
                vc += 1
                coords.append(c)
    return vc, coords


def nextpoint(cv, bounds) -> (bool, tuple):
    # cv is a list contianing x, y initial velocity, bounds is a list of bounding tuples
    cp = [0,0]
    iv = (cv[0], cv[1])
    while True:
        cp[0] += cv[0]
        cp[1] += cv[1]
        if inbounds(cp, bounds):
            if inbounds(cp, bounds):
                return True, iv
        if cp[1] < bounds[1][1]:
            return False, iv
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
    r.append(1)
    r.append(xhigher + 1)
    return r

def yfactors(bounds) -> list:
    r = []
    ylower = bounds[1][1]
    r.append(ylower)
    r.append(abs(ylower))
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
