# returns sqrt(f) when f is non-negative
def sqrt(f: float) -> float:
    if f < 0:
        raise ValueError('f must be positive')
    return f ** 0.5


def test_sqrt():
    assert sqrt(4.0) == 2.0


test_sqrt()

