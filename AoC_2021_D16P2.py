from inp import day16 as data
from timeit import Timer

bin = """0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111"""

# data = "9C0141080250320F1802104A08"

def prod(ls) -> int:
    out = ls[0]
    for x in ls[1:]:
        out *= x
    return out

def setupbin(bin) -> dict:
    binmap = {}
    b = bin.split("\n")
    for x in b:
        binmap[x[0]] = x[-4:]
    return binmap

def setupdata(data, bin) -> (str, dict):
    out = ""
    b = setupbin(bin)
    for i in range(len(data)):
        out += b[data[i]]
    return out, b


def runner(sdata):
    bm = sdata[1]
    sdata = sdata[0]
    sdata, out = bigparser(bm, sdata)
    return out


def bigparser(bm, sdata):
    out = 0
    if len(sdata) > 6:
        ver = "0" + sdata[:3]
        typ = "0" + sdata[3:6]
        sdata = sdata[6:]
        if typ == "0100":
            sdata, out = literal(sdata)
        else:
            if sdata[0] == "0":
                ls = []
                subpacketslen = int(sdata[1:16], 2)
                sdata = sdata[16:]
                subpackets = sdata[:subpacketslen]
                sdata = sdata[subpacketslen:]
                while True:
                    subpackets, l = bigparser(bm, subpackets)
                    ls += [l]
                    if len(subpackets) < 6:
                        break
                out = operation(ls, typ, bm)

            else:
                ls = []
                subcount = int(sdata[1:12], 2)
                subpackcount = 0
                sdata = sdata[12:]
                while subpackcount < subcount:
                    sdata, l = bigparser(bm, sdata)
                    subpackcount += 1
                    ls += [l]
                out = operation(ls, typ, bm)

    return  sdata, out

def literal(sdata) -> (str, int):
    chunks = []
    chunking = True
    while chunking:
        chunks += [sdata[:5]]
        sdata = sdata[5:]
        if chunks[-1][0] == '0':
            chunking = False
    l = int(''.join([x[1:] for x in chunks]), 2)
    return sdata, l

def operation(ls, typ, bm) -> int:
    op = int([k for k, v in bm.items() if v == typ ][0])
    print(op, ls)
    if op == 0:
        return sum(ls)
    elif op == 1:
        return prod(ls)
    elif op == 2:
        return min(ls)
    elif op == 3:
        return max(ls)
    elif op == 5:
        return 1 if ls[0] > ls[1] else 0
    elif op == 6:
        return 1 if ls[0] < ls[1] else 0
    elif op == 7:
        return 1 if ls[0] == ls[1] else 0

if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(data, bin)))
    print(t.timeit(number=1))
    print(runner(setupdata(data, bin)))
