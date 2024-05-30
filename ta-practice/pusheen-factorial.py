"""
Pusheen factorial
Similar to a normal factorial calculation, but if n is odd,
only the sum of odd numbers will be used to calculate the
factorial. If n is even, only the sum of even numbers will
be used to calculate the factorial.
"""


def is_even(n: int) -> int:
    """
    Helper function to check if n is even
    """
    return n % 2 == 0


def push_fac(n: int):
    # Edge case 1
    if n < 0:
        return -1

    # Edge case 2
    if n == 0:
        return 1

    total_sum = 0

    # Loop that starts with n and then decreases by 1
    # with each pass
    for i in range(n, 0, -1):
        num = None

        # If n is even, then only use even numbers in the calculation
        if is_even(i) and is_even(n):
            num = i

        # If n is odd, then only use odd numbers in the calculation
        if not is_even(i) and not is_even(n):
            num = i
        
        if num:
            if total_sum == 0:
                total_sum = num
            else:
                total_sum = total_sum * num

    return total_sum


def test_push_fac():
    assert push_fac(-1) == -1
    assert push_fac(0) == 1
    assert push_fac(7) == 105
    assert push_fac(10) == 3840
    assert push_fac(19) == 654729075


test_push_fac()