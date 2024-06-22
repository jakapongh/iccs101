# Assignment 4, Task 6
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 10 mins


def sumOfDigitsSquared(n: int) -> int:
    sum = 0
    for char in str(n):
        sum += int(char) ** 2
    return sum


def isHappy(n: int) -> bool:
    # have x
    # if x = 1 || 4, stop
    # else: continue
    # get the sum of the squares of each digit
    # repeat until 1 or 4
    if n <= 0:
        return False

    while n != 1 and n != 4:
        n = sumOfDigitsSquared(n)

    if n == 1:
        # happy
        return True
    elif n == 4:
        # sad
        return False


def kThHappy(k: int) -> int:
    # test all happy numbers
    i = 0
    current_happy_idx = 0
    current_happy = None
    # add to all_happies until we reach k index
    while current_happy_idx != k:
        if isHappy(i):
            current_happy = i
            current_happy_idx += 1

        i += 1

    return current_happy


def test_all():
    assert sumOfDigitsSquared(7) == 49
    assert sumOfDigitsSquared(145) == 42
    assert sumOfDigitsSquared(199) == 163

    assert isHappy(100) is True
    assert isHappy(111) is False
    assert isHappy(1234) is False
    assert isHappy(989) is True

    assert kThHappy(1) == 1
    assert kThHappy(3) == 10
    assert kThHappy(11) == 49
    assert kThHappy(19) == 97
