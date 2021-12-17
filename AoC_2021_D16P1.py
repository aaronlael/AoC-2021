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
    print(sdata)
    return bigparser(bm, sdata)


def bigparser(bm, sdata):
    vcount = 0
    if len(sdata) > 6:
        ver = "0" + sdata[:3]
        typ = "0" + sdata[3:6]
        print(ver, typ)
        vcount += int([k for k, v in bm.items() if v == ver ][0])
        sdata = sdata[6:]
        if typ == "0100":
            sdata = literal(sdata)
        else:
            if sdata[0] == "0":
                subpacketslen = int(sdata[1:16], 2)
                sdata = sdata[16:]
                subpackets = sdata[:subpacketslen]
                sdata = sdata[subpacketslen:]
                subcount = 0
                while True:
                    t, subpackets = bigparser(bm, subpackets)
                    subcount += t
                    if len(subpackets) < 6:
                        break
                vcount += subcount

            else:
                subcount = int(sdata[1:12], 2)
                subpackcount = 0
                vercount = 0
                sdata = sdata[12:]
                while subpackcount < subcount:
                    t, sdata = bigparser(bm, sdata)
                    vercount += t
                    subpackcount += 1
                vcount += vercount

    return vcount, sdata

def literal(sdata):
    t = 5
    chunks = []
    chunking = True
    while chunking:
        chunks += [sdata[:5]]
        sdata = sdata[5:]
        if chunks[-1][0] == '0':
            chunking = False
            print(chunks)
    return sdata

if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(data, bin)))
    print(t.timeit(number=1))
    print(runner(setupdata(data, bin)))
