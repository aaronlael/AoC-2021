from inp import day20_inp as data, day20_key
from timeit import Timer

# day20_key = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"


def setupdata(data):
    sdata = data.split("\n")
    return sdata


def runner(sdata):
    # p1
    # runs = 2
    # p2
    runs = 50
    sdata = processor(sdata)
    for r in range(runs):
        pd = []
        for y in range(len(sdata)):
            r = ""
            for x in range(len(sdata[y])):
                r += day20_key[lookaround(sdata,x,y)]
            pd.append(r)
        sdata = pd
    # p1
    # sdata = [x[50:-50] for x in sdata[50:-50]]
    # P2
    sdata = [x[50:-50] for x in sdata[50:-50]]
    return lightcount(sdata)


def lightcount(sdata) -> int:
    lc = 0
    for row in sdata:
        lc += row.count("#")
    return lc


def processor(sdata) -> list:
    out = []
    # prepare the data for infinite possibilities
    sdata = [ "." * 200 + x + "." * 200 for x in sdata]
    rowbuffer = ["." * len(sdata[0])]
    for x in range(200):
        sdata = rowbuffer + sdata + rowbuffer
    return sdata


def lookaround(sdata, x, y) -> int:
    b = ""
    # top left
    ty = y - 1
    tx = x -1
    if ty >= 0 and tx >= 0:
        b+= "0" if sdata[ty][tx] == "." else "1"
    else:
        b+= "0"
    # top
    tx = x
    if ty >= 0:
        b+= "0" if sdata[ty][tx] == "." else "1"
    else:
        b+= "0"
    # top right
    tx = x + 1
    if ty >= 0 and tx < len(sdata[0]):
        b+= "0" if sdata[ty][tx] == "." else "1"
    else:
        b+= "0"
    # left
    ty = y
    tx = x - 1
    if tx >= 0:
        b+= "0" if sdata[ty][tx] == "." else "1"
    else:
        b+= "0"
    # center
    b+= "0" if sdata[y][x] == "." else "1"
    # right
    tx = x + 1
    if tx < len(sdata[0]):
        b+= "0" if sdata[ty][tx] == "." else "1"
    else:
        b+= "0"
    # bottom left
    ty = y + 1
    tx = x -1
    if ty < len(sdata) and tx >= 0:
        b+= "0" if sdata[ty][tx] == "." else "1"
    else:
        b+= "0"
    # bottom
    tx = x
    if ty < len(sdata):
        b+= "0" if sdata[ty][tx] == "." else "1"
    else:
        b+= "0"
    # bottom right
    tx = x + 1
    if ty < len(sdata) and tx < len(sdata[0]):
        b+= "0" if sdata[ty][tx] == "." else "1"
    else:
        b+= "0"
    return int(b, 2)

if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(data)))
    print(t.timeit(number=1))
    print(runner(setupdata(data)))
