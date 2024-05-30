def coinChange(v: int) -> list[int]:
    # Gives
    # dispensed
    # always give out coin with the largest available
    # value first and repeat until full amount is made

    # infinite supply of $10, $5, $2, $1

    accumulator = []
    remaining = v

    tens = remaining // 10
    remaining -= tens * 10

    fives = remaining // 5
    remaining -= fives * 5

    twos = remaining // 2
    remaining -= twos * 2

    ones = remaining // 1
    remaining -= ones * 1

    accumulator += repeating_nums(10, tens)
    accumulator += repeating_nums(5, fives)
    accumulator += repeating_nums(2, twos)
    accumulator += repeating_nums(1, ones)

    return accumulator


def repeating_nums(val: int, n: int):
    arr = []
    for i in range(n):
        arr.append(val)

    return arr


def test_coinChange():
    assert coinChange(38) == [10, 10, 10, 5, 2, 1]
    assert coinChange(19) == [10, 5, 2, 2]
    assert coinChange(11) == [10, 1]
    assert coinChange(5) == [5]
    assert coinChange(3) == [2, 1]


test_coinChange()
