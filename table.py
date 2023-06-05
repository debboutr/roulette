from random import randint

RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]

BLACK = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 29, 31, 33, 35]
# (10,11) (19,20) (27,28)

# STREETS = {
#         "01": [1,2,3],
#         "02": [4,5,6],
#         "03": [7,8,9],
#         "04": [10,11,12],
#         "05": [13,14,15],
#         "06": [16,17,18],
#         "07": [19,20,21],
#         "08": [22,23,24],
#         "09": [25,26,27],
#         "10": [28,29,30],
#         "11": [31,32,33],
#         "12": [34,35,36]
#         }


def md(num, iter):
    z = zip([f"{i:02d}" for i in range(1, num)], iter)
    return {k: v for k, v in z}


SQ = [[n + 1, n + 2, n + 4, n + 5] for n in range(0, 31, 3)]
STREETS = md(13, [[i + r for r in range(3)] for i in range(1, 35, 3)])
CORNERS = md(23, [p for q in zip(SQ, [[n + 1 for n in b] for b in SQ]) for p in q])
# D - double street | S - street | C -Column | T - third | B- Black | R - red
# H - High | L - Low | E - even | O - odd
COLUMNS = md(4, [list(range(1, 37, 3)), list(range(2, 37, 3)), list(range(3, 37, 3))])
# COLUMNS = {
#         "01": list(range(1,37,3)),
#         "02": list(range(2,37,3)),
#         "03": list(range(3,37,3)),
#         }

THIRDS = {
    "A": list(range(1, 13)),
    "B": list(range(13, 25)),
    "C": list(range(25, 36)),
}


class Table:
    number = None

    def __init__(self, lays):
        self.lays = []
        self.play = 0
        self._load_bets(lays.split("|"))

    def _load_bet(self, bet):
        self.lays.append(bet.split(":"))

    def _load_bets(self, iter):
        for i in iter:
            self._load_bet(i)

    def roll(self):
        self.number = randint(0, 37)
        # print(f"Spin number: {self.number}")

    def payout(self):
        total = 0
        self.play = sum([int(wager) for _, wager in self.lays])
        hits = ""
        for bet, wager in self.lays:
            wager = int(wager)
            # print(bet, wager)
            if bet[0] == "C":
                if self.number in COLUMNS[bet[1]]:
                    total += 3 * wager
            if bet[0] == "T":
                if self.number in THIRDS[bet[1]]:
                    total += 3 * wager
            if bet[0] == "D":
                total += self.street_pay(bet[1:], wager)
            if bet[0] == "S":
                total += self.street_pay(bet[1:], wager)
            if bet[0] == "E":
                if self.number % 2 == 0 and self.number > 0:
                    total += 2 * wager
            if bet[0] == "O":
                if self.number % 2 == 1 and self.number != 37:
                    total += 2 * wager
            if bet[0] == "H":
                if 18 < self.number < 37:
                    total += 2 * wager
            if bet[0] == "L":
                if 0 < self.number < 19:
                    total += 2 * wager
            if bet[0] == "R":
                if self.number in RED:
                    total += 2 * wager
            if bet[0] == "B":
                if self.number in BLACK:
                    total += 2 * wager
        # print(f"total: {total}")
        # print(f"play: {self.play}")
        return total - self.play

    def street_pay(self, street, wager):
        if len(street) == 4:
            for i, s in enumerate([street[:2], street[2:]]):
                if self.number in STREETS[s]:
                    return wager * 6
                elif i == 0:
                    continue
                else:
                    return 0
        elif self.number in STREETS[street]:
            return wager * 11
        else:
            return 0


if __name__ == "__main__":
    table = Table()
    table.load("H:1000|L:1000|D0203:22|S01:33|TA:50|CB:50")
    # print(table.bets)
    table.roll()
    table.payout()


#
# LIMIT = 500
#
# def roll():
#    return randint(1,38)
#
#
# def play(bet):
#    if roll() in range(19,37):
#        return bet
#    else:
#        return 0
#
#
# def five_in_a_row():
#    aa = []
#    rolls = [play(1) for _ in range(1000)]
#    for i in range(len(rolls) - 5 + 1):
#        if sum(rolls[i:i+5]) == 0:
#            aa.append(1)
#    return sum(aa)
#
#
# def run_game():
#    seq = [3, 6, 18, 54, 162]
#    index = 0
#    stack = 243
#    loss = 0
#    win = []
#    spins = []
#    spin = 0
#    for _ in range(1_000):
#        spin += 1
#        res = play(seq[index])
#        if res > 0:
#            index = 0
#            stack += res
#        else:
#            stack -= seq[index]
#            index += 1
#        if index == 5 and res == 0 and stack < 162:
#            loss += 1
#            stack = 243
#            index = 0
#            spin = 0
#        elif index == 5 and res == 0:
#            index = 4
#        if stack >= LIMIT:
#            # import pdb
#            # pdb.set_trace()
#            win += [stack -243]
#            stack = 243
#            index = 0
#            spins += [spin]
#            spin = 0
#    print (
#        f"WIN: ${sum(win):,}\n"
#        f"LOSE: ${loss*243:,}\n"
#        f"WINS: {len(win)}\n"
#        f"LOSSES: {loss}\n"
#        # f"MAX: {max(win)}\n"
#        # f"MIN: {min(win)}\n"
#        # f"MEAN: {mean(win)}\n"
#        f"STACK: {stack}\n"
#        f"WINS: {win}\n"
#        # f"SPINS: {spins}"
#        )
