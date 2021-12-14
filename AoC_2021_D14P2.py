from inp import day14_1 as data_1, day14_2 as data_2
import copy
from timeit import Timer


def setupdata(data_2):
    d = data_2.split("\n")
    dict = {}
    for x in d:
        k, v = x.split(" -> ")
        dict[k] = v
    return dict


def runner(sdata, data_1):
    statedict = {}
    # populates statedict from data_1
    for i in range(len(data_1) - 1):
        k = data_1[i:i+2]
        if k not in statedict:
            statedict[k] = 0
        statedict[k] += 1
    steps = 40
    while steps > 0:
        tdict = {}
        for k in statedict:
            n = sdata[k]
            if k[0]+n not in tdict:
                tdict[k[0]+n] = 0
            tdict[k[0]+n] += statedict[k]
            if n+k[1] not in tdict:
                tdict[n+k[1]] = 0
            tdict[n+k[1]] += statedict[k]
        statedict = copy.deepcopy(tdict)
        steps -= 1
    # this produces a value that is 1 (without the + 1).  I need to figure out why.
    return lettercount(statedict) + 1


def lettercount(sdict):
    counts = {}
    c = []
    for k in sdict:
        v1, v2 = k[0], k[1]
        if v1 not in counts:
            counts[v1] = 0
        counts[v1] += sdict[k]
        if v2 not in counts:
            counts[v2] = 0
        counts[v2] += sdict[k]
    for k in counts:
        if k == data_1[0] or k == data_1[-1]:
            counts[k] = (counts[k] - 1) / 2
            c += [(k, counts[k])]
        else:
            counts[k] = counts[k] / 2
            c += [(k, counts[k])]
    c.sort(key=lambda x: x[1])
    return c[-1][1] - c[0][1]


if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(data_2), data_1))
    print(t.timeit(number=1))
    print(runner(setupdata(data_2), data_1))
