def has_three(n: int):
    # Given an integer n, how many numbers from 1 to n
    # has 3 as a digit
    three_counts = 0

    for i in range(n + 1):
        i_str = str(i)
        three_counts += i_str.count("3")

    return three_counts


def test_has_three():
    assert has_three(3) == 1
    assert has_three(12) == 1
    assert has_three(15) == 2
    assert has_three(32) == 6


test_has_three()
