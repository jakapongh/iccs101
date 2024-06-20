def count_a(s: str) -> int:
    if s == '': return 0
    keep = s[0]
    rest = s[1:]
    friend_answer = count_a(rest)

    if keep == 'a':
        return friend_answer + 1
    return friend_answer


print(count_a('baaahjufuashfw9qwkdfklmaaakssja'))
