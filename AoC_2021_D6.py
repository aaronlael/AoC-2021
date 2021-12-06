from inp import day6
from timeit import Timer


def setupdata(data):
    return data.split(",")

def dayrunner(data):
    # part 1
    # days = 80
    # part 2
    days = 256
    d = {}
    for e in data:
        d = dictpopulate(e,1,d)
    print(d)
    for i in range(days):
        t = {}
        for i in range(9):
            t[str(i)] = 0
        for k in d:
            if k == "0":
                t["6"] += d[k]
                t["8"] += d[k]
            else:
                tk = str(int(k) - 1)
                t[tk] += d[k]
        d = t.copy()
    c = 0
    for k in d:
        c += int(d[k])
    print(d)
    return c


def dictpopulate(k, v, d):
    td = d.copy()
    if k not in td:
        td[k] = 0
    td[k] += int(v)
    return td


if __name__ == '__main__':
    t = Timer(lambda: dayrunner(setupdata(day6)))
    print(t.timeit(number=1))
    print(dayrunner(setupdata(day6)))
