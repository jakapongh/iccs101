# Assignment 3, Task 1
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 5 min


def my_min(p: float, q: float, r: float) -> float:
    # returns the minimum of three numbers
    lowest = p
    if q < lowest: lowest = q
    if r < lowest: lowest = r
    return lowest


def my_mean(p: float, q: float, r: float) -> float:
    res = (p + q + r)/3
    return res



def my_med(p: float, q: float, r: float) -> float:
    # get max first and remove the min and max to get middle
    min = my_min(p, q, r)
    max = p

    if q > max: max = p
    if r > max: max = r

    mid = (p + q + r) - min - max

    return mid

def test():
    assert my_mean(1, 2, 3) == 2
    assert my_min(3.0, 1.0, 9.0) == 1.0
    assert my_med(4.0, 1.0, 5.0) == 4.0
    assert my_med(13.0, 5.0, 12.0) == 12.0

test()