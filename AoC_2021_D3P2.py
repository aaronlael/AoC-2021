from inp import day3
from timeit import Timer


def setupdata(data):
    return data.split("\n")


def binpos(sdata, i, mode):
    out = []
    vals = [x[i] for x in sdata]
    if mode == "o2":
        if vals.count("0") > vals.count("1"):
            out = [x for x in sdata if x[i] == "0"]
        else:
            out = [x for x in sdata if x[i] == "1"]
    else:
        if vals.count("0") > vals.count("1"):
            out = [x for x in sdata if x[i] == "1"]
        else:
            out = [x for x in sdata if x[i] == "0"]
    return out


def binrunner(sdata):
    oxy = sdata
    co2 = sdata
    for i in range(len(sdata[0])):
        if len(oxy) > 1:
            oxy = binpos(oxy, i, "o2")
        if len(co2) > 1:
            co2 = binpos(co2, i, "co2")
        if len(co2) == 1 and len(oxy) == 1:
            return(int(oxy[0], 2) * int(co2[0], 2))
    else:
        return "You dun goofed A-A-ron"


if __name__ == '__main__':
    t = Timer(lambda: binrunner(setupdata(day3)))
    print(t.timeit(number=1))
    print(binrunner(setupdata(day3)))
