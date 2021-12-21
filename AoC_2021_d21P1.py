from inp import day21 as data
from timeit import Timer


def setupdata(data):
    sdata = data.split("\n")
    return { "1" : {"pos" : int(sdata[0][-1]),
                    "score" : 0,
                    },
            "2" : { "pos" : int(sdata[1][-1]),
                    "score" : 0,
                    }
            }


def runner(sdata):
    i = 0
    rolling = True
    while rolling:
        for p in ["1", "2"]:
            d1, d2, d3 = i+1, i+2, i+3
            i += 3
            sdata[p]["pos"] = roll(d1, d2, d3, sdata, p)
            if sdata[p]["pos"] == 0:
                sdata[p]["score"] += 10
            else:
                sdata[p]["score"] += sdata[p]["pos"]
            if sdata[p]["score"] >= 1000:
                rolling = False
                break

    for k in sdata:
        if sdata[k]["score"] > 1000:
            print("Winner", k)
        else:
            print("Loser", k, sdata[k]["score"] * i)
    return sdata, i


def roll(d1, d2, d3, sdata, p) -> int:
    return (d1 + d2 + d3 +sdata[p]["pos"]) % 10


if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(data)))
    print(t.timeit(number=1))
    print(runner(setupdata(data)))
