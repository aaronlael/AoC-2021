from inp import day1
from AoC_2021_D1P1 import setupdata
from timeit import Timer

def windowincreasing(data):
    ic = 0
    cache = {}
    for i in range(1,len(data)-2):
        if str(i-1) not in cache:
            cache[str(i-1)] = sum([int(x) for x in [data[i-1], data[i], data[i+1]]])
        if str(i) not in cache:
            cache[str(i)] = sum([int(x) for x in [data[i], data[i+1], data[i+2]]])
        if cache[str(i)] > cache[str(i-1)]:
            ic += 1
    return ic



if __name__ == '__main__':
    t = Timer(lambda: windowincreasing(setupdata(day1)))
    print(t.timeit(number=1))
    print(windowincreasing(setupdata(day1)))
