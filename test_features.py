from table import Table, Chip, RED, BLACK, Bets


# def test_table_roll():
#     t = Table()
#     assert t.number == None
#     t.roll()
#     assert 0 < t.number < 37
#     t = Table()
#     t.roll()
#     assert t.rolls == 2


# def test_again():
#     t = Table("33:D:0405|44:E")
#     assert t.bets == [["D0405","33"], ["E","44"]]
#     assert t.rolls == 2


def test_bets():
    b = Bets("10:D:0405|45:E")
    for x in b:
        assert isinstance(x, Chip)
    assert len(b.bets) == 2
    assert b.sum() == 55


def test_payout():
    t = Table("10:S:04|45:O")
    t.number = 12
    assert t.payout() == 65
