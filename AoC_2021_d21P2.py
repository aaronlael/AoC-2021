from inp import day21 as data
from copy import deepcopy
import itertools
from timeit import Timer

dirolls = list(itertools.product([1,2,3], repeat=3))


def setupdata(data) -> dict:
    sdata = data.split("\n")
    return { "1" : {"pos" : int(sdata[0][-1]),
                    "score" : 0,
                    },
            "2" : { "pos" : int(sdata[1][-1]),
                    "score" : 0,
                    }
            }

def runner(sdata) -> dict:
    games = {}
    winners = { "1": 0,
                "2": 0
                }
    rolling = True
    games[gamestate(sdata)] = 1
    while rolling:
        out = {}
        for game in games:
            g = unformat(game)
            drolls = roll(g, "1")
            for k in drolls:
                if k not in out:
                    out[k] = drolls[k] * games[game]
                else:
                    out[k] += drolls[k] * games[game]
        for game in out:
            g = unformat(game)
            if g["1"]["score"] >= 21:
                winners["1"] += out[game]
                out[game] = 0
        out = {k:v for k,v in out.items() if v != 0}
        tout = {}
        for game in out:
            g = unformat(game)
            drolls = roll(g, "2")
            for k in drolls:
                if k not in tout:
                    tout[k] = drolls[k] * out[game]
                else:
                    tout[k] += drolls[k] * out[game]
        for game in tout:
            g = unformat(game)
            if g["2"]["score"] >= 21:
                winners["2"] += tout[game]
                tout[game] = 0
        tout = {k:v for k,v in tout.items() if v != 0}
        games = deepcopy(tout)
        if len(games) == 0:
            rolling = False
    if winners["1"] > winners["2"]:
        return winners["1"]
    else:
        return winners["2"]


def roll(game, p) -> dict:
    out = {}
    for v in dirolls:
        g = deepcopy(game)
        g[p]["pos"] = (g[p]["pos"] + sum(v)) % 10
        if g[p]["pos"] == 0:
            g[p]["score"] += 10
        else:
            g[p]["score"] += g[p]["pos"]
        g = gamestate(g)
        if g not in out:
            out[g] = 1
        else:
            out[g] += 1
    return out

def gamestate(game) -> str:
    # player1|position p1|score p1| player2 | position p2 | score p2
    return f"""1|{game["1"]["pos"]}|{game["1"]["score"]}|2|{game["2"]["pos"]}|{game["2"]["score"]}"""

def unformat(gamestate) -> dict:
    g = gamestate.split("|")
    d = { "1" : {"pos" : int(g[1]),
                    "score" : int(g[2]),
                    },
            "2" : { "pos" : int(g[4]),
                    "score" : int(g[5]),
                    }
            }
    return d


if __name__ == '__main__':
    t = Timer(lambda: runner(setupdata(data)))
    print(t.timeit(number=1))
    print(runner(setupdata(data)))
