from inp import day7
from timeit import Timer


def setupdata(data):
    return data.split(",")


def main(data):
    sdata = [int(x) for x in setupdata(data)]
    d = {}
    for i in range(min(sdata), max(sdata)):
        for s in sdata:
            if str(i) not in d:
                d[str(i)] = 0
            dist = abs(s - i)
            d[str(i)] += int(((1+dist)/2)*dist)
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    return d[list(d.keys())[0]]


if __name__ == '__main__':
    t = Timer(lambda: main(day7))
    print(t.timeit(number=1))
    print(main(day7))
