def has_size(order_size: int, sizes: list[int]):
    for size in sizes:
        if order_size == size:
            return True
    return False


def constructable(order_size: int, sizes: list[int]):
    # See if the order can be constructed from the
    # given sizes
    for i in range(len(sizes)):
        size_one = sizes[i]
        for j in range(len(sizes)):
            size_two = sizes[j]
            if size_one + size_two == order_size:
                return True
    return False


def processOrders(orders: list[int], sizes: list[int]) -> list[bool]:
    """
    orders represents lengths requested
    sizes represents sizes carried by the store
    Returns: a list of booleans, i-th element is whether or not i-th order
    can be fulfilled
    """
    fulfilled = []
    # Fits exactly
    for order in orders:
        if has_size(order, sizes) or constructable(order, sizes):
            fulfilled.append(True)
        else:
            fulfilled.append(False)
    return fulfilled


def test_processOrders():
    assert (processOrders([5, 7, 13], [3, 5, 6, 10]) == [True, False, True])
    assert (processOrders([5, 12, 13, 20], [1, 2, 5, 10])
            == [True, True, False, True])
    assert (processOrders([9, 116, 169], [20, 23, 32, 36])
            == [False, False, False])
    assert (processOrders([9, 13, 39, 128, 184, 187], [
        13, 15, 19, 20, 22, 27, 33, 40, 43, 45]) == [False, True, True, False, False, False])
    assert (processOrders([28, 29, 60, 88, 117, 133, 140, 144, 160], [3, 5, 7, 11, 14, 16, 20, 22,
                                                                      24, 26, 32, 34, 42, 43]) == [True, True, True,
                                                                                                   False, False, False,
                                                                                                   False, False, False])
    assert (processOrders([4, 7, 16, 21, 43, 64, 77, 83, 106, 116, 165, 182], [6, 8, 10, 14, 18, 20, 25, 27, 33, 34,
                                                                               36, 37, 43, 44, 47, 48, 49]) == [False,
                                                                                                                False,
                                                                                                                True,
                                                                                                                False,
                                                                                                                True,
                                                                                                                True,
                                                                                                                True,
                                                                                                                True,
                                                                                                                False,
                                                                                                                False,
                                                                                                                False,
                                                                                                                False])
    assert (processOrders([17, 21, 63, 68, 77, 83, 84, 92, 114, 134, 151, 162, 163, 165, 184],
                          [1, 2, 4, 6, 8, 10, 11, 13, 16, 19, 20, 21, 23,
                           26, 28, 29, 38, 39, 40, 41, 45]) == [True, True, True, True, True, True, True, False, False,
                                                                False, False, False, False, False, False])


test_processOrders()