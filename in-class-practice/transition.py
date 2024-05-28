def transition(L: list[int]) -> int:
    # Given a list of integers, find out how many
    # times there are transitions from odd to even
    # in the list
    transitions_count = 0
    last_is_even = None

    for n in L:
        current_is_even = n % 2 == 0
        if (not last_is_even and current_is_even) and last_is_even is not None:
            transitions_count += 1

        last_is_even = current_is_even

    return transitions_count


def test_transition():
    assert transition([1, 2, 4, 5]) == 1
    assert transition([1, 5, 7]) == 0
    assert transition([]) == 0


test_transition()
