# Assignment 4, Task 5
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 1 min


def allMultiplesOfK(k: int, lst: list[int]) -> bool:
    is_multiple = True
    for n in lst:
        if n % k != 0:
            is_multiple = False
    return is_multiple

def test_allMultiplesOfK():
    assert allMultiplesOfK(4, [1,10,20]) is False
    assert allMultiplesOfK(3, [81,3,24]) is True
    assert allMultiplesOfK(11, []) is True


test_allMultiplesOfK()
