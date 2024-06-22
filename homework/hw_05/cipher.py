# Assignment 05, Task 03
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 50 mins

def str_to_rows(msg: str, key: int) -> list[list[str]]:
    rows = []
    char_idx = 0
    row_len = 0
    col = []

    while char_idx < len(msg):
        if row_len == key:
            row_len = 0
            rows.append(col)
            col = []
        else:
            col.append(msg[char_idx])
            row_len += 1
            char_idx += 1

    # Append last col
    rows.append(col)
    return rows


def enc(msg: str, key: int) -> str:
    rows = str_to_rows(msg, key)
    combined = ""
    col_idx = 0
    while col_idx < key:
        row_idx = 0
        while row_idx < len(rows):
            if col_idx < (len(rows[row_idx])):
                char = rows[row_idx][col_idx]
                combined += char
            row_idx += 1
        col_idx += 1

    return combined


def test_enc():
    assert enc("abc", 2) == 'acb'
    assert enc("monosodium glutamate", 7) == 'mitouanmmo asgtoledu'
    assert enc("polylogarithmicsubexponential", 3) == 'pygimseonaolatiuxntllorhcbpei'


test_enc()
