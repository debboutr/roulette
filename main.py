import click
from table import Table


def play_strategy():
    total = 120
    rolls = 0
    walk = 240
    while total < walk and total >= 60:
        rolls += 1
        # print("spin")
        table = Table("D0102:30|D0304:20|D0506:20|D0708:20|D0910:30")

        # print(f"PLAY: {table.play}")
        # table.load("H:1000|L:1000|D0203:22|S01:33|TA:50|CB:50")
        # table.load()
        # print(table.bets)
        table.roll()
        total += table.payout()
        # print(f"TOTAL: {total}")
    if total >= walk:
        print(f"rolls: {rolls} || {total} || WIN!!")
        return 1
    if total < 30:
        print(f"rolls: {rolls} || {total} || LOSE")
        return 0


def play_strategy2():
    total = 1000
    rolls = 0
    b = 10
    while total < 1150 and total >= 0:
        rolls += 1
        # print("spin")
        table = Table(f"TA:{b}|TB:{b}")

        # print(f"PLAY: {table.play}")
        # table.load("H:1000|L:1000|D0203:22|S01:33|TA:50|CB:50")
        # table.load()
        # print(table.bets)
        table.roll()
        pay = table.payout()
        # print(f"TOTAL: {pay}", f"{b}", f"{total}")
        if pay < 0:
            b += 10
        total += pay

    if total >= 1150:
        # print(f"rolls: {rolls} || WIN!!")
        return 1
    if total <= 0:
        # print(f"rolls: {rolls} || LOSE")
        return 0


# table.load("H:10|B:10|TB:10|CB:10")
wins = []
NO = 10_000
for n, _ in enumerate(range(NO)):
    # print(f"GAME: {n}")
    rr = play_strategy()
    wins.append(rr)
    # if rr:
    # print("WIN!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # else:
    # print("LOSE!!!!!!!!!!!!!!!!!!!!!!!!!!")

print("OUT:", sum(wins) / NO)
