from inp import day3
from timeit import Timer


def setupdata(data):
    return data.split("\n")


def binsort(sdata):
    vals = {}
    gamma = ""
    eps = ""
    for x in sdata:
        for i in range(len(x)):
            if str(i) not in vals:
                vals[str(i)] = []
            vals[str(i)] += [x[i]]
    for i in range(len(sdata[0])):
        if vals[str(i)].count("0") > vals[str(i)].count("1"):
            gamma += "0"
            eps += "1"
        else:
            gamma += "1"
            eps += "0"
    return int(gamma, 2) * int(eps, 2)


if __name__ == '__main__':
    t = Timer(lambda: binsort(setupdata(day3)))
    print(t.timeit(number=1))
    print(binsort(setupdata(day3)))
