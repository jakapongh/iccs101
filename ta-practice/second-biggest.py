# "Pusheen Prize Hunt" - fun name, but it's basically a function
# that returns the second-biggest number in a list
# CHALLENGE: You are only allowed to loop through the list once

def second_biggest(lst: list[int]) -> int:
    current_biggest = max(lst)
    current_second_biggest = lst[0]
    current_second_biggest_idx = 0

    for idx, num in enumerate(lst):
        if current_second_biggest < num < current_biggest:
            current_second_biggest = num
            current_second_biggest_idx = idx

    return current_second_biggest_idx


# Tests
def test_second_biggest():
    assert second_biggest([12, 25, 7, 19, 3, 30, 14, 8]) == 1
    assert second_biggest([27, 5, 18, 22, 9, 30, 11, 6]) == 0
    assert second_biggest([15, 0, 28, 20, 4, 13, 29, 7]) == 2


test_second_biggest()