# Assignment 07, Task 01
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: -


def all_perm(n: int) -> set[tuple[int, ...]]:
    if n == 1:
        return {(1,)}

    smaller_perms = all_perm(n - 1)
    result = set()

    for perm in smaller_perms:
        for i in range(n):
            new_perm = perm[:i] + (n,) + perm[i:]
            result.add(new_perm)

    return result


print(all_perm(3))
