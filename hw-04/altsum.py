# Assignment 4, Task 1
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 5 mins


def altSum(lst: list[int]) -> int:
    collector = 0

    for idx, n in enumerate(lst):
        if idx != 0 and idx % 2 == 0:
            n = n * -1
        collector += n

    return collector

def test_altSum():
    assert altSum([]) == 0
    assert altSum([1, 3, 5, 2]) == 1
    assert altSum([7, 7, 7, 7]) == 14
    assert altSum([31, 4, 28, 5, 71]) == -59


test_altSum()