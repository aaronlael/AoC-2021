from inp import day12
from timeit import Timer


def setupdata(data):
    t = data.split("\n")
    for i in range(len(t)):
        if "start" in t[i]:
            if t[i][:5] != 'start':
                t[i] = "-".join(t[i].split("-")[::-1])
        if "end" in t[i]:
            if t[i][:3] != 'end':
                t[i] = "-".join(t[i].split("-")[::-1])
    return t


def runner(sdata):
    points = pointdict(sdata)
    b = branches(points)
    vb = [b[x] for x in b if b[x][-1] != 'bad']
    return(len(vb))


def pointdict(sdata):
    d = {}
    for x in sdata:
        t = x.split("-")
        if t[0] not in d:
            d[t[0]] = [t[1]]
        else:
            d[t[0]] += [t[1]]
    for x in sdata:
        t = x.split("-")
        if t[0] != 'start' and t[1] != 'end':
            if t[1] not in d:
                d[t[1]] = [t[0]]
            else:
                d[t[1]] += [t[0]]
    return d


def branches(d):
    br = {}
    i = 0
    s = d['start']
    for x in s:
        br[str(i)] = ['start', x]
        i += 1
    branching = True
    while branching:
        for j in range(len(br)):
            j = str(j)
            if br[j][-1] != 'end' and br[j][-1] != 'bad':
                newbranches = d[br[j][-1]]
                nbl = len(newbranches)
                for n in range(len(newbranches)):
                    if n == nbl - 1:
                        br[j] += [newbranches[n]]
                    else:
                        br[str(i)] = br[j] + [newbranches[n]]
                        i += 1
        for j in range(len(br)):
            j = str(j)
            if not branchvalid(br[j]) and br[j][-1] != 'bad':
                br[j] += ['bad']
        if branchend(br):
            branching = False

    return br


def branchend(d):
    for b in d:
        if d[b][-1] != 'end' and d[b][-1] != 'bad':
            return False
    return True


def branchvalid(b):
    sb = set(b)
    morethanone = 0
    for s in sb:
        if s.lower() == s:
            if b.count(s) > 2:
                return False
            if b.count(s) == 2:
                morethanone += 1
    if morethanone > 1:
        return False
    return True


if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(day12)))
    print(t.timeit(number=1))
    print(runner(setupdata(day12)))
