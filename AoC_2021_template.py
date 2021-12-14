# from inp import day as data
from timeit import Timer

data = ""

def setupdata(data):
    return data.split("\n")


def runner(sdata):
    print(sdata)


if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(data)))
    print(t.timeit(number=1))
    print(runner(setupdata(data)))
