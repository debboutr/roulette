import click
from table import Table


def play_strategy3():
    rolls = 0
    walk = 1600
    total = 1000
    i = 0
    amount = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    while total < walk and total > 0:
        rolls += 1
        table = Table(f"TA:{amount[i]}|TB:{amount[i]}")
        table.roll()
        pay = table.payout()
        if pay > 0:
            i -= 1
            i = 0 if i < 0 else i
            total += pay
            print(f"rolls: {rolls} || {total} || WIN!!")
        if pay == 0:
            i += 1
            print(f"rolls: {rolls} || {total} || LOSE!!")
    if total >= walk:
        print(f"rolls: {rolls} || {total} || WIN!!")
        return 1
    if total < 30:
        print(f"rolls: {rolls} || {total} || LOSE")
        return 0


def play_strategy():
    total = 120
    rolls = 0
    walk = 240
    while total < walk and total > 100:
        rolls += 1
        # print("spin")
        table = Table("30:D:0102|20:D:0304|20:D:0506|20:D:0708|30:D:0910")

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
    if total < 100:
        print(f"rolls: {rolls} || {total} || LOSE")
        return 0


def play_strategy2():
    total = 1000
    rolls = 0
    b = 10
    while total < 1150 and total >= 0:
        rolls += 1
        # print("spin")
        table = Table(f"{b}:T:01|{b}:T:02")

        # print(f"PLAY: {table.play}")
        # table.load("H:1000|L:1000|D0203:22|S01:33|TA:50|CB:50")
        # table.load()
        # print(table.bets)
        table.roll()
        pay = table.payout()
        if pay < 0:
            b += 10
        total += pay

    if total >= 1150:
        # print(f"rolls: {rolls} || WIN!!")
        return 1
    if total <= 0:
        print(f"TOTAL: {pay}", f"{rolls}", f"{total}")
        # print(f"rolls: {rolls} || LOSE")
        return 0


wins = []
NO = 100
for n, _ in enumerate(range(NO)):
    rr = play_strategy2()
    wins.append(rr)

print("OUT:", sum(wins) / NO)
