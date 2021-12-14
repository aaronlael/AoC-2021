from inp import day14_1 as data_1, day14_2 as data_2
from timeit import Timer


def setupdata(data_2):
    d = data_2.split("\n")
    dict = {}
    for x in d:
        k, v = x.split(" -> ")
        dict[k] = v
    return dict


def runner(sdata, data_1):
    data_1
    temp = ""
    steps = 10
    while steps > 0:
        for i in range(len(data_1) - 1):
            new = sdata[data_1[i:i+2]]
            temp += data_1[i] + new
        temp += data_1[-1]
        data_1 = temp
        temp = ""
        steps -= 1
    s = set(list(data_1))
    od = []
    for x in s:
        od.append((x, data_1.count(x)))
    od.sort(key=lambda x: x[1])
    return od[-1][1] - od[0][1]


if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(data_2), data_1))
    print(t.timeit(number=1))
    print(runner(setupdata(data_2), data_1))
