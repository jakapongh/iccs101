# Assignment 05, Task 05
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 4 hours

# Used to see how much time execution took
import time

def is_word_in_char_list(word: str, char_list: list[str]) -> bool:
    accum = ""
    for col in char_list:
        accum += col
        if word in accum:
            return True

    return False


def get_diagonals(grid: list[list[str]]) -> list[list[str]]:
    # Diagonal
    # Transformation: each diagonal line becomes its own row
    grid_diagonal = []

    """
        x are items that will be checked
    
        x - - - - - - -
        x x - - - - - -
        x x x - - - - -
        x x x x - - - -
        x x x x x - - -
        x x x x x x - -
        x x x x x x x -
        x x x x x x x x
    """
    # Traverse from top left to bottom left
    for main_row_idx in range(len(grid)):
        new_row = []
        for row_idx in range(len(grid)):
            pos = row_idx - main_row_idx
            if pos >= 0:
                char = grid[row_idx][pos]
                new_row.append(char)
        grid_diagonal.append(new_row)

    # Traverse from top left to top right
    """
        x are items that will be checked
        
        x x x x x x x x
        - x x x x x x x
        - - x x x x x x
        - - - x x x x x
        - - - - x x x x
        - - - - - x x x
        - - - - - - x x
        - - - - - - - x
    """
    for col_idx in range(len(grid[0])):
        new_row = []
        for row_idx in range(len(grid)):
            pos = row_idx + col_idx
            if pos < len(grid[row_idx]):
                char = grid[row_idx][pos]
                new_row.append(char)
        grid_diagonal.append(new_row)

    return grid_diagonal


def get_verticals(grid: list[list[str]]) -> list[list[str]]:
    # Linear vertical
    # Transformation: each column becomes its own row
    grid_vertical = []
    no_columns = len(grid[0])
    for existing_col_idx in range(no_columns):
        new_row = []
        for existing_row in grid:
            new_row.append(existing_row[existing_col_idx])

        grid_vertical.append(new_row)

    return grid_vertical


def word_sleuth(grid: list[list[str]], words: list[str]) -> list[str]:
    execution_start_time = time.time()

    all_word_combinations = []

    # Linear horizontal
    all_word_combinations += grid

    # Linear vertical
    all_word_combinations += get_verticals(grid)

    # Diagonals
    all_word_combinations += get_diagonals(grid)

    # Search for words in all combinations
    words_found = []
    for current_word in words:
        for combination in all_word_combinations:
            if is_word_in_char_list(current_word, combination) and current_word not in words_found:
                words_found.append(current_word)

    print(words_found)
    execution_end_time = time.time()
    execution_time_ms = (execution_end_time - execution_start_time) * 1000
    print(f"Execution took {execution_time_ms:.4f} ms")
    return words_found


def test_word_sleuth():
    # Using sorted() so it's order-agnostic
    assert word_sleuth([["r","a","w","b","i","t"],
                ["x","a","y","z","c","h"],
                ["p","q","b","e","i","e"],
                ["t","r","s","b","o","g"],
                ["u","w","x","v","i","t"],
                ["n","m","r","w","o","t"]],
                sorted(["bog", "moon", "rabbit", "the", "bit", "raw"])) == sorted(["raw", "bit","rabbit", "bog", "the"])


test_word_sleuth()
