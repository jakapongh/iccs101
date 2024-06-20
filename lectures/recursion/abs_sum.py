def abs_sum(L: list[int]):
    # return the sum of all absolute values of all
    # elements
    if len(L) == 0: return 0
    keep = L[0]
    rest = L[1:]

    friend_answer = abs_sum(rest)
    friend_answer += abs(keep)
    return friend_answer

print(abs_sum([-1, 2, -5, 10]))
