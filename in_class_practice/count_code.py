def count_code(msg: str) -> int:
    # count number of times string "code"
    # appears anywhere in the string
    # or any variation where the d is replaced
    # by another character

    count = 0
    collector = ""
    for str_idx in range(len(msg)):
        collector += msg[str_idx]

        # check occurrences of "code"
        if "code" in collector:
            count += 1
            collector = ""

        # check occurrences of
        # "co[?]e"
        if "co" in collector:
            if (str_idx + 2) <= (len(msg) - 1):
                if msg[str_idx + 2] == 'e':
                    count += 1
                    collector = ""
    return count


# OPTIMAL SOLUTION
def count_code_OPTIMAL(msg: str) -> int:
    count = 0

    for i in range(len(msg) - 3):
        if msg[i:i+2] == "co" and msg[i+3] == "e":
            count += 1

    return count


def test_count_code():
    assert count_code_OPTIMAL('aaacodebbb') == 1
    assert count_code_OPTIMAL('codexxcode') == 2
    assert count_code_OPTIMAL('cozexxcope') == 2
    assert count_code_OPTIMAL('codecooecopeccccome') == 4


test_count_code()
