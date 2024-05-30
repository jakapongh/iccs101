def valid_id(idnum: str) -> bool:
    # multiply each digit by its digit position
    # digit position = how far it is from right
    # add up products of all digits
    # EXCEPT rightmost digit

    c = 0
    for idx, digit in enumerate(idnum):
        # do not add the rightmost
        if idx == len(idnum) - 1:
            continue
        rightmost_position = len(idnum) - idx
        c += rightmost_position * int(digit)

    a = (11 - c % 11) % 10
    return int(idnum[-1]) == a


def test_valid_id():
    assert (valid_id('180628621489758') is True)
    assert (valid_id('606228772259487') is False)
    assert (valid_id('729921769655535') is True)
    assert (valid_id('171009540283809') is False)
    assert (valid_id('123045607890126') is True)
    assert (valid_id('648986931487827') is False)


test_valid_id()
