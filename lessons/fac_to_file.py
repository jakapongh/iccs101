def fac_to_file(n: int, filename: str) -> None:
    accum = 0
    for i in range(1, n):
        if accum == 0:
            accum = 1
        accum = accum * n
        print(i)
    print(accum)



fac_to_file(10, 'test.out')
