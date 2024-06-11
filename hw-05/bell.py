# Assignment 05, Task 01
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 2 hours


def loveTri(n: int) -> list[list[int]]:
    rows = []
    for row_idx in range(n):
        row = []

        # Get last row
        if not len(rows):
            # If rows are empty, first row will be 1
            last_row = [1]
        else:
            last_row = rows[-1]

        # Append last number of last row
        row.append(last_row[-1])

        # Add last column's number to current column
        # Start from last row's num until current row's index + 1
        for col_idx in range(row_idx):
            # current row's column
            current_row_col = row[col_idx]
            row.append(last_row[col_idx] + current_row_col)

        rows.append(row)
    print(rows)
    return rows


def test_loveTri():
    assert loveTri(5) == [
        [1],
        [1, 2],
        [2, 3, 5],
        [5, 7, 10, 15],
        [15, 20, 27, 37, 52]
    ]

test_loveTri()
