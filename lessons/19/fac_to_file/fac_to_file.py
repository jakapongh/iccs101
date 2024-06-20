# Recursive factorial function
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


def fac_to_file(n: int, filename: str) -> None:
    with open(filename, 'w') as f:
        f.write(str(factorial(n)))


fac_to_file(10, 'test.out')
