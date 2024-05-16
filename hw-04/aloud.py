# Assignment 4, Task 4
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 1 hour

# This surprisingly took me a long time. I think the code
# could be simpler. Maybe do it again?


def readAloud(lst: list[int]) -> list[int]:
    new_lst = []
    parent_idx = 0

    # Use while loop as opposed to for loops so that we can
    # set the index to our liking

    # We want to avoid checking the items we have already
    # checked in the second loop. Being able to set the
    # index to our liking is an advantage.

    while parent_idx < len(lst):
        current_count = 0
        parent = lst[parent_idx]
        child_idx = parent_idx

        while child_idx < len(lst):
            child = lst[child_idx]

            if parent == child:
                current_count += 1

                # Avoid checking the same number we have
                # already checked in child loop
                child_idx += 1
                parent_idx = child_idx
            else:
                # Parent is not same as child, this is a
                # different number, therefore restart
                # parent loop to check the current,
                # different number.

                # child_idx - 1 cancels out the parent_idx
                # += 1 below in parent loop, which results
                # in the parent checking the current,
                # different number.

                parent_idx = child_idx - 1
                break

        new_lst.append(current_count)
        new_lst.append(parent)
        parent_idx += 1

    return new_lst


def test_readAloud():
    assert readAloud([]) == []
    assert readAloud([1, 1, 1]) == [3, 1]
    assert readAloud([-1, 2, 7]) == [1, -1, 1, 2, 1, 7]
    assert readAloud([3, 3, 8, -10, -10, -10]) == [2, 3, 1, 8, 3, -10]
    assert readAloud([3, 3, 1, 1, 3, 1, 1]) == [2, 3, 2, 1, 1, 3, 2, 1]


test_readAloud()
