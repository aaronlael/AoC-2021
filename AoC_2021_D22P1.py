# from inp import day22 as data
from timeit import Timer

data = """on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13"""


def setupdata(data):
    out = []
    d = data.split("\n")
    for x in d:
        t = {"func": "", "x1": 0, "x2": 0, "y1": 0, "y2": 0, "z1": 0, "z2": 0}
        xchunks = x.split(" ")
        t["func"] = xchunks[0]
        xchunks = xchunks[1].split(",")
        for c in xchunks:
            coord = c[0]
            crange = c[2:].split("..")
            t[coord + "1"] = int(crange[0])
            t[coord + "2"] = int(crange[1])
        out.append(t)
    return out


def runner(sdata):
    on = []
    for f in sdata:
        t = []
        dim = ((f["x1"], f["y1"], f["z1"]), (f["x2"], f["y2"], f["z2"]))
        if len(on) == 0:
            on.append(dim)
        else:
            for cube in on:
                # new cube x min within existing cube
                if cube[0][0] <= dim[0][0] and cube[1][0] >= dim[1][0]:
                    pass
    return len(on)


if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(data)))
    print(t.timeit(number=1))
    print(runner(setupdata(data)))
