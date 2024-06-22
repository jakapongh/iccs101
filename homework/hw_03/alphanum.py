# Assignment 3, Task 5
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 5 mins

def charToNum(char):
    char = char.upper()

    if char in "ABC": return "2"
    if char in "DEF": return "3"
    if char in "GHI": return "4"
    if char in "JKL": return "5"
    if char in "MNO": return "6"
    if char in "PQRS": return "7"
    if char in "TUV": return "8"
    if char in "WXYZ": return "9"

    return char


def phoneWord2Num(word: str) -> int:
    collector = ""
    collector += charToNum(word[0])
    collector += charToNum(word[1])
    collector += charToNum(word[2])
    collector += charToNum(word[3])
    collector += charToNum(word[4])
    collector += charToNum(word[5])
    collector += charToNum(word[6])

    return int(collector)


def test_phoneWord2Num():
    assert phoneWord2Num("FLOWERS") == 3569377
    assert phoneWord2Num("PrOGrAM") == 7764726
    assert phoneWord2Num("Battery") == 2288379


test_phoneWord2Num()