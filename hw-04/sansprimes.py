# Assignment 4, Task 7
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False

    return result


def sans_primes(numbers: list[int]) -> list[int]:
    new_list = []
    i = 0
    while i < len(numbers):
        number = numbers[i]
        if is_prime(number):
            # Skip next num if not at end of list
            if i + 1 <= (len(numbers) - 1):
                i += 1
        else:
            new_list.append(number)

        i += 1
    print(new_list)
    return new_list


def test_all():
    # assert is_prime(1) is False
    # assert is_prime(2) is True
    # assert is_prime(-2) is False
    # assert is_prime(5) is True
    # assert is_prime(41) is True
    # assert is_prime(323) is False
    #
    # assert sans_primes([1, 4, 9, 10]) == [1, 4, 9, 10]
    # assert sans_primes([1, 11, 9, 10, 17]) == [1, 10]
    # assert sans_primes([3, 10, 2, 8, 9, 4, 1, 7, 6, 5, 11]) == [9, 4, 1]
    # assert sans_primes([3, 1, 2, 4]) == []
    assert sans_primes([3, -2, 5, 7, 1, 42]) == [42]
    assert sans_primes([1, 0, 3, 0, -2, 5, 7, 1, 42, 9]) == [1, 0, -2, 42, 9]


test_all()
