# Assignment 3, Task 3
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 15 mins


def kthDigit(x: int, b: int, k: int) -> list:
    latest_remainder = None
    latest_quotient = x
    collector = []

    # No idea how to do it without using loops

    while latest_quotient != 0:
        remainder = latest_quotient % b
        latest_quotient = latest_quotient // b
        collector.insert(0, remainder)

    # If position of number out of range, return 0
    if k > len(collector) - 1: return 0

    return collector[len(collector) - 1 - k]


def test_kthDigit():
    assert kthDigit(789, 10, 0) == 9
    assert kthDigit(789, 10, 1) == 8
    assert kthDigit(789, 10, 2) == 7
    assert kthDigit(789, 10, 3) == 0

    assert kthDigit(987, 16, 0) == 11
    assert kthDigit(987, 16, 1) == 13
    assert kthDigit(987, 16, 2) == 3


test_kthDigit()