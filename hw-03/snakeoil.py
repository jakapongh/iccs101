# Assignment 3, Task 2
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 10 min


def price(vol: int) -> float:
    shipping_price = 0
    product_price = vol * 18

    if 0 < vol < 20:
        shipping_price = 250

    if 20 <= vol <= 100:
        shipping_price = 10 * vol

    if vol > 100:
        product_price = product_price * 0.99

    return shipping_price + product_price


def test_price():
    assert price(0) == 0
    assert price(5) == 340.0
    assert price(20) == 560.0
    assert price(200) == 3564.0


test_price()
