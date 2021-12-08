from inp import day8
from timeit import Timer


def setupdata(data):
    return data.split("\n")


def main(data):
    dout = {}
    sdata = setupdata(data)
    for sd in sdata:
        sp, ov = sd.split(" | ")
        sp = sp.split(" ")
        ov = ov.split(" ")
        t = signaldecode(sp, ov)
        for val in t:
            if val not in dout:
                dout[val] = 0
            dout[val] += 1

    output = dout["1"] + dout["4"] + dout["7"] + dout["8"]
    return output


def signaldecode(pattern, output):
    rubric = {}
    for x in pattern:
        if len(x) == 2:
            rubric["1"] = sorted(list(x))
        elif len(x) == 3:
            rubric["7"] = sorted(list(x))
        elif len(x) == 4:
            rubric["4"] = sorted(list(x))
        elif len(x) == 7:
            rubric["8"] = sorted(list(x))
    for x in pattern:
        if len(x) == 5:
            if len(set.intersection(set(list(x)), set(rubric["1"]))) == 2:
                rubric["3"] = sorted(list(x))
            elif len(set.intersection(set(list(x)), set(rubric["4"]))) == 3:
                rubric["5"] = sorted(list(x))
            else:
                rubric["2"] = sorted(list(x))
    for x in pattern:
        if len(x) == 6:
            if len(set.intersection(set(list(x)), set(rubric["1"]))) == 1:
                rubric["6"] = sorted(list(x))
            elif len(set.intersection(set(list(x)), set(rubric["4"]))) == 4:
                rubric["9"] = sorted(list(x))
            else:
                rubric["0"] = sorted(list(x))
    out = []
    for x in output:
        xl = sorted(list(x))
        for k in rubric:
            if xl == rubric[k]:
                out += [k]
    return out


if __name__ == '__main__':
    t = Timer(lambda: main(day8))
    print(t.timeit(number=1))
    print(main(day8))
