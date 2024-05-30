# Constant definitions of what constitutes
# as vowels and alphabets
VOWELS = "aeiou"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def is_upper(char: str):
    """
    Checks if a character is uppercase
    """
    return char.upper() == char


def better_swap_case(st: str) -> str:
    # Turn the string into a list of characters so that we
    # can directly replace a character at a given position
    # to another character
    st_list = list(st)

    for idx, char in enumerate(st_list):
        # We do .lower() on the character for normalisation
        # because "A" != "a". In this case we don't care about the
        # casing therefore we'll just make it lowercase.

        if char.lower() not in ALPHABET:
            # Characters that aren't in the alphabet (e.g. numbers)
            # will be replaced with a space
            char = " "
        elif char.lower() not in VOWELS:
            # Characters that aren't vowels
            # If the character is uppercase, it will be turned into
            # lowercase and vice versa
            if is_upper(char):
                char = char.lower()
            else:
                char = char.upper()

        # Now that we have performed the necessary actions on the character,
        # we'll put the changed character back into it's original place
        st_list[idx] = char

    # Takes all the characters in st_list and join them back together
    # into a normal string
    result = "".join(st_list)

    return result


# Tests
def test_better_swap_case():
    assert better_swap_case('WbS') == 'wBs'
    assert better_swap_case('XUOfuN') == 'xUOFun'
    assert better_swap_case('OpFuod') == 'OPfuoD'
    assert better_swap_case('pGHa') == 'Pgha'
    assert better_swap_case('uMHruZY7') == 'umhRuzy '
    assert better_swap_case('EkbrEO:=l') == 'EKBREO  L'
    assert better_swap_case('I)oQ0ZLCJ') == 'I oq zlcj'
    assert better_swap_case('iO5^uia') == 'iO  uia'
    assert better_swap_case('v6q`uiI2') == 'V Q uiI '
    assert better_swap_case('E2;RoF~3') == 'E  rof  '


test_better_swap_case()
