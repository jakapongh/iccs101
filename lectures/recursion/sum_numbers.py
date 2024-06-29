def sum(l: list) -> int:
    if len(l) == 1:
        return l[0]

    keep = l[0]
    rest = l[1:]
    friend_answer = sum(rest)
    friend_answer += keep
    return friend_answer


print(sum([1, 2, 3, 4]))
