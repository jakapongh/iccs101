def rec_min(L: list[float]) -> float:
    if len(L) == 1:
        return L[0]

    keep = L[0]
    friend_answer = rec_min(L[1:])
    if keep < friend_answer:
        return keep
    else:
        return friend_answer


print(rec_min([1.0, -1.0, -8.0, 10.0]))
