from inp import day18 as data
import ast
from timeit import Timer


nums = "1234567890"


def setupdata(data) -> list:
    return data.split("\n")



def runner(sdata):
    base = ""
    for line in sdata:
        if base != "":
            line = "[" + base + "," + line + "]"
        while True:
            line, f = explodes(line)
            if not f:
                line, s = splits(line)
            if not f and not s:
                base = line
                break

    mag = ast.literal_eval(base)
    return magnitude(mag)


def explodes(line) -> (str, int):
    expflag = 0
    for i in range(len(line)):
        if line[i] in nums:
            if nesting(i, line) > 4:
                expflag = 1
                # identify exploding pair bounds
                lbound = i-1
                for b in range(i, len(line)):
                    if line[b] == "]":
                        rbound = b
                        break
                # convert chunk to actual list to extract values easily
                exp = ast.literal_eval(line[lbound: rbound + 1])
                le = exp[0]
                re = exp[1]
                # left explode
                lleft = line[:lbound]
                lright = line[rbound + 1:]
                for ln in reversed(range(len(lleft))):
                    if lleft[ln] in nums:
                        # 2 digit number receiving explosion
                        if lleft[ln-1] in nums:
                            v = int(lleft[ln-1:ln+1])
                            v += int(le)
                            lleft = lleft[:ln-1] + str(v) + lleft[ln+1:]
                        else:
                            v = int(lleft[ln])
                            v += int(le)
                            lleft = lleft[:ln] + str(v) + lleft[ln+1:]
                        break
                # right explodes
                for rn in range(len(lright)):
                    if lright[rn] in nums:
                        # 2 digit number receiving explosion
                        if lright[rn+1] in nums:
                            v = int(lright[rn:rn+2])
                            v += int(re)
                            lright = lright[:rn] + str(v) + lright[rn+2:]
                        else:
                            v = int(lright[rn])
                            v += int(re)
                            lright = lright[:rn] + str(v) + lright[rn+1:]
                        break
                line = lleft + "0" + lright
                # print("exp - " + line)
                break
    return line, expflag


def splits(line) -> (str, int):
    spflag = 0
    for i in range(len(line)):
        if line[i] in nums:
            if line[i+1] in nums:
                spflag = 1
                n = int(line[i:i+2])
                l = n // 2
                r = n - l
                line = line[:i] + f"[{l},{r}]" + line[i+2:]
                # print("Spl - " + line)
                break
    return line, spflag


def nesting(i, line):
    rcount = line[:i].count("]")
    lcount = line[:i].count("[")
    return lcount - rcount


def magnitude(l) -> int:
    m = 0
    for i in range(len(l)):
        if type(l[i]) == list:
             l[i] = magnitude(l[i])
    else:
        if len(l) == 2:
            m += int(l[0]) * 3
            m += int(l[1]) * 2
        else:
            m += int(l[0])
    return m


if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(data)))
    print(t.timeit(number=1))
    print(runner(setupdata(data)))
