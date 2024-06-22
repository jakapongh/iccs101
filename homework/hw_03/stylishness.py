# Assignment 3, Task 7
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 4 mins


def got_table(you: int, date: int) -> str:
    if you <= 2 or date <= 2:
        return "no"

    if you >= 8 or date >= 8:
        return "yes"

    return "maybe"


def test_got_table():
    assert got_table(7, 3) == "maybe"
    assert got_table(9, 4) == "yes"
    assert got_table(7, 8) == "yes"
    assert got_table(1, 10) == "no"


test_got_table()
