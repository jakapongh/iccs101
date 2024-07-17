# Assignment 07, Task 01
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: a day


def all_perm(n: int) -> set[tuple[int, ...]]:
    if n == 1:
        # base case
        return {(1,)}
    else:
        # recursive case, generate permutations for n-1
        prev_perms = all_perm(n - 1)
        perms = set()
        for prev_perm in prev_perms:
            # go through each possible position to insert n
            for i in range(n):
                new_perm = prev_perm[:i] + (n,) + prev_perm[i:]  # insert n into position i of prev_perm
                perms.add(new_perm)
        return perms


def test():
    assert all_perm(2) == {(1, 2), (2, 1)}
    assert all_perm(3) == {(3, 1, 2), (1, 3, 2), (1, 2, 3), (3, 2, 1), (2, 3, 1), (2, 1, 3)}
    assert all_perm(4) == {(4, 3, 1, 2), (3, 4, 1, 2), (3, 1, 4, 2), (3, 1, 2, 4),
                    (4, 1, 3, 2), (1, 4, 3, 2), (1, 3, 4, 2), (1, 3, 2, 4),
                    (4, 1, 2, 3), (1, 4, 2, 3), (1, 2, 4, 3), (1, 2, 3, 4),
                    (4, 3, 2, 1), (3, 4, 2, 1), (3, 2, 4, 1), (3, 2, 1, 4),
                    (4, 2, 3, 1), (2, 4, 3, 1), (2, 3, 4, 1), (2, 3, 1, 4),
                    (4, 2, 1, 3), (2, 4, 1, 3), (2, 1, 4, 3), (2, 1, 3, 4)}


test()
