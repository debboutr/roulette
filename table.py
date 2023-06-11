from random import randint
from dataclasses import dataclass


def md(num, iter):
    z = zip([f"{i:02d}" for i in range(1, num)], iter)
    return {k: v for k, v in z}


def pump(x, y, z=1):
    return list(range(x, y, z))


HIGH = pump(19, 37)
LOW = pump(1, 19)
EVEN = [x for x in range(1, 37) if not x % 2]
ODD = [x for x in range(1, 37) if x % 2]
RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]
BLACK = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 29, 31, 33, 35]

STREETS = md(13, [[i + r for r in range(3)] for i in range(1, 35, 3)])
SQ = [[n + 1, n + 2, n + 4, n + 5] for n in range(0, 31, 3)]
COLUMNS = md(4, [pump(x, 37, 3) for x in [1, 2, 3]])
THIRDS = md(4, [pump(x, y) for x, y in [(1, 13), (13, 25), (25, 36)]])
CORNERS = md(23, [p for q in zip(SQ, [[n + 1 for n in b] for b in SQ]) for p in q])

INSIDE = {
    "C": COLUMNS,
    "T": THIRDS,
}

OUTSIDE = {
    "B": BLACK,
    "R": RED,
    "H": HIGH,
    "L": LOW,
    "E": EVEN,
    "O": ODD,
}


@dataclass
class Chip:
    value: int
    aim: str
    loc: str = ""


class Bets:
    def __init__(self, plays=""):
        self.bets = self._load_bets(plays.split("|"))

    def __iter__(self):
        yield from self.bets

    def _load_bets(self, it):
        plays = []
        for i in it:
            l = i.split(":")
            l[0] = int(l[0])
            plays.append(Chip(*tuple(l)))
        return plays

    def sum(self):
        return sum([c.value for c in self.bets])


class User:
    ...


class Strategy:
    ...


class Table:
    number = None
    rolls = 0

    def __init__(self, plays=""):
        self.bets = []
        self.play = 0
        self.total = 0
        self.bets = Bets(plays)

    def roll(self):
        Table.rolls += 1
        self.number = randint(0, 37)

    def check_hit(self, c, l_dict, scale=2):
        x = c.aim if scale == 2 else c.loc
        if self.number in l_dict[x]:
            self.total += scale * c.value

    def payout(self):
        for c in self.bets:
            if c.aim in ["D", "S"]:
                self.total += self.street_pay(c)
            if c.aim in INSIDE.keys():
                d = INSIDE[c.aim]
                print(d)
                self.check_hit(c, d, scale=3)
            if c.aim in OUTSIDE.keys():
                self.check_hit(c, OUTSIDE)
        return self.total - self.bets.sum()

    def street_pay(self, c):
        if len(c.loc) == 4:
            for i, s in enumerate([c.loc[:2], c.loc[2:]]):
                if self.number in STREETS[s]:
                    return c.value * 6
                elif i == 0:
                    continue
                else:
                    return 0
        elif self.number in STREETS[c.loc]:
            return c.value * 12
        else:
            return 0


if __name__ == "__main__":
    table = Table()
    table.load("H:1000|L:1000|D0203:22|S01:33|TA:50|CB:50")
    # print(table.bets)
    table.roll()
    table.payout()

"""
----AIMS----
D - double street
S - street
C - column
N - corner
T - third
B - black
R - red
H - High
L - Low
E - even
O - odd

----[[ LOCS ]]----
----STREETS----
"01": [1,2,3],
"02": [4,5,6],
"03": [7,8,9],
"04": [10,11,12],
"05": [13,14,15],
"06": [16,17,18],
"07": [19,20,21],
"08": [22,23,24],
"09": [25,26,27],
"10": [28,29,30],
"11": [31,32,33],
"12": [34,35,36]

----CORNERS----
'01': [1, 2, 4, 5],
'02': [2, 3, 5, 6],
'03': [4, 5, 7, 8],
'04': [5, 6, 8, 9],
'05': [7, 8, 10, 11],
'06': [8, 9, 11, 12],
'07': [10, 11, 13, 14],
'08': [11, 12, 14, 15],
'09': [13, 14, 16, 17],
'10': [14, 15, 17, 18],
'11': [16, 17, 19, 20],
'12': [17, 18, 20, 21],
'13': [19, 20, 22, 23],
'14': [20, 21, 23, 24],
'15': [22, 23, 25, 26],
'16': [23, 24, 26, 27],
'17': [25, 26, 28, 29],
'18': [26, 27, 29, 30],
'19': [28, 29, 31, 32],
'20': [29, 30, 32, 33],
'21': [31, 32, 34, 35],
'22': [32, 33, 35, 36]

----COLUMNS----
"01": list(range(1,37,3)),
"02": list(range(2,37,3)),
"03": list(range(3,37,3)),
"""
