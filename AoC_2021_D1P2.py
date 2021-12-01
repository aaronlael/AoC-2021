from inp import day1
from AoC_2021_D1P1 import setupdata

def windowincreasing(data):
    ic = 0
    for i in range(1,len(data)-2):
        psum = sum([int(x) for x in [data[i-1], data[i], data[i+1]]])
        csum = sum([int(x) for x in [data[i], data[i+1], data[i+2]]])
        if csum > psum:
            ic += 1
    return ic



if __name__ == '__main__':
    print(windowincreasing(setupdata(day1)))
