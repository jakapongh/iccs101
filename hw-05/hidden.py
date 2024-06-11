# Assignment 05, Task 02
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 10 mins

def is_hidden(s: str, t: str) -> bool:
    t_idx = 0
    s_idx = 0
    s = s.lower()
    t = t.lower()

    reconstruction = ""

    while t_idx < len(t) and s_idx < len(s):
        char_looking_for = t[t_idx]

        if s[s_idx] == char_looking_for:
            t_idx += 1
            reconstruction += char_looking_for

        s_idx += 1

    return reconstruction == t


def test_is_hidden():
    assert is_hidden("welcometothehotelcalifornia", "melon") == True
    assert is_hidden("welcometothehotelcalifornia", "space") == False
    assert is_hidden("TQ89MnQU3IC7t6", "MUIC") == True
    assert is_hidden("VhHTdipc07", "htc") == True
    assert is_hidden("VhHTdipc07", "hTc") == True
    assert is_hidden("VhHTdipc07", "vat") == False


test_is_hidden()
