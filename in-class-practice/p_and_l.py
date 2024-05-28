def p_and_l(L: list[float]) -> int:
    """
    given daily profit and loss of shop
    report how many days high profit or high loss
    high is when loss or gain is greater than average
    ignore 0
    """

    total_loss = 0
    days_loss = 0

    total_profit = 0
    days_profit = 0

    # find total loss/profit and days with loss/profit
    for n in L:
        if n < 0:
            total_loss += n
            days_loss += 1
        elif n > 0:
            total_profit += n
            days_profit += 1

    avg_loss = total_loss / days_loss
    avg_profit = total_profit / days_profit

    days_high_loss = 0
    days_high_profit = 0

    for n in L:
        if n < avg_loss:
            # high loss
            days_high_loss += 1
        elif n > avg_profit:
            # high profit
            days_high_profit += 1

    result = days_high_loss + days_high_profit
    return result


def test_p_and_l():
    assert p_and_l([1.0, -1.0, 1.0, -1.0, 100.0, -50.0]) == 2


test_p_and_l()
