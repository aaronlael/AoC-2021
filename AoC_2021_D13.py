from inp import day13_1, day13_2
from timeit import Timer


def setupdata(d_1, d_2):
    d_1 = [(int(x.split(",")[0]), (int(x.split(",")[1])))
           for x in d_1.split("\n")]
    d_2 = [x.replace("fold along ", "") for x in d_2.split("\n")]
    return d_1, d_2


def runner(coords, folds):
    coords, folds = setupdata(coords, folds)
    paper = buildpaper(coords)
    # part 1
    paper = foldpaper(paper, folds[0])
    pcount = 0
    for y in range(len(paper)):
        for x in paper[y]:
            if x == "#":
                pcount += 1
    print(f"part 1 answer: {pcount}")
    # part 2
    for fold in folds:
        paper = foldpaper(paper, fold)
    for p in paper:
        print("".join(p).replace(".", " "))
    return "part 2 answer ^^^"


def buildpaper(coords):
    xmax = max([x[0] for x in coords]) + 1
    ymax = max([x[1] for x in coords]) + 1
    row = ["." for x in range(xmax)]
    paper = []
    # I added one here, it fixed the output text and I think I know why...
    for i in range(ymax + 1):
        paper.append([x for x in row])
    for coord in coords:
        paper[coord[1]][coord[0]] = "#"
    return paper


def foldpaper(paper, fold):
    foldaxis = fold[0]
    foldval = int(fold[2:])
    if foldaxis == "y":
        below = paper[foldval + 1:][::-1]
        above = paper[:foldval]
        for i in range(len(below)):
            for j in range(len(below[i])):
                if below[i][j] == "#":
                    above[i][j] = "#"
        return above
    else:
        right = [[x for x in y[foldval + 1:][::-1]] for y in paper]
        left = [[x for x in y[:foldval]] for y in paper]
        for i in range(len(right)):
            for j in range(len(right[i])):
                if right[i][j] == "#":
                    left[i][j] = "#"
    return left


if __name__ == '__main__':
    t = Timer(lambda: runner(day13_1, day13_2))
    print(t.timeit(number=1))
    print(runner(day13_1, day13_2))
