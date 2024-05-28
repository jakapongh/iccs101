# do factorial, but pusheen is angry
# earse some numbers
# erase all numbers in sequence based on parity
# if n is odd, all nums of factorial is odd
# and vice versa

def is_even(n):
    return n % 2 == 0


def push_fac(n: int):
    if n < 0:
        return -1

    if n == 0:
        return 1

    total = 0
    for i in range(n, 0, -1):
        num = None

        if is_even(i) and is_even(n):
            num = i

        if not is_even(i) and not is_even(n):
            num = i

        if num:
            if total == 0:
                total = num
            else:
                total = total * num

    return total


def test_push_fac():
    assert push_fac(-1) == -1
    assert push_fac(0) == 1
    assert push_fac(7) == 105
    assert push_fac(10) == 3840
    assert push_fac(19) == 654729075


test_push_fac()