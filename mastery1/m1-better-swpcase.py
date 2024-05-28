VOWELS = "aeiou"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def is_upper(char: str):
    return char.upper() == char


def better_swap_case(st: str) -> str:
    st_list = list(st)

    for idx, char in enumerate(st_list):
        if char.lower() not in ALPHABET:
            # replace with space
            char = " "
        elif char.lower() not in VOWELS:
            if is_upper(char):
                char = char.lower()
            else:
                char = char.upper()

        st_list[idx] = char
    result = "".join(st_list)
    return result


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
