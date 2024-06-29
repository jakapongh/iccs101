# Assignment 06, Task 06
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: 4 hours
# ----------------------------------
from typing import List, Tuple

Board = List[List[str]]

# Checks whether a given board has any
# possible move left. If no more moves,
# return True. Otherwise return False.


def isGameOver(board: Board) -> bool:
    return len(emptyPos(board)) == 0

# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Up' key.


def is_empty(col):
    return col == " "


def has_empty_between(board: Board, direction: str) -> bool:
    # direction = ENUM("right", "left", "up", "down")

    if direction == "right":
        # Left to right
        for row_idx in range(len(board)):
            row = board[row_idx]
            for col_idx in range(len(row) - 2, -1, -1):
                if not is_empty(row[col_idx]) and is_empty(row[col_idx + 1]):
                    # Current col not empty and next col empty
                    return True
    elif direction == "left":
        # Right to left
        for row_idx in range(len(board)):
            row = board[row_idx]
            for col_idx in range(len(row) - 1, 0, -1):
                if not is_empty(row[col_idx]) and is_empty(row[col_idx - 1]):
                    # Current col not empty and next col empty
                    return True
    elif direction == "up":
        # Down to up
        for row_idx in range(len(board) - 1, 0, -1):
            row = board[row_idx]
            for col_idx in range(len(row)):
                if not is_empty(board[row_idx][col_idx]) and is_empty(board[row_idx - 1][col_idx]):
                    # Current col not empty and above col empty
                    return True
    elif direction == "down":
        # Up to down
        for row_idx in range(len(board) - 1):
            row = board[row_idx]
            for col_idx in range(len(row) - 1):
                if not is_empty(board[row_idx][col_idx]) and is_empty(board[row_idx + 1][col_idx]):
                    # Current col not empty and col below empty
                    return True
    return False


def compact_tiles(board: Board, direction: str) -> Tuple[bool, Board]:
    # direction = ENUM("right", "left", "up", "down")

    board_changed = False
    if direction == "right":
        while has_empty_between(board, direction):
            for row_idx, row in enumerate(board):
                for col_idx, col in enumerate(row):
                    if not is_empty(col):
                        # Current col not empty
                        if col_idx == len(board[row_idx]) - 1:
                            # Last column, skip
                            continue
                        if is_empty(board[row_idx][col_idx + 1]):
                            # Column to the right is empty
                            # Move the number to the right
                            board_changed = True
                            board[row_idx][col_idx + 1] = board[row_idx][col_idx]
                            board[row_idx][col_idx] = " "
    elif direction == "left":
        while has_empty_between(board, direction):
            for row_idx, row in enumerate(board):
                for col_idx, col in enumerate(row):
                    if is_empty(col):
                        # Current col empty
                        if col_idx == len(board[row_idx]) - 1:
                            # Last column, skip
                            continue
                        if not is_empty(board[row_idx][col_idx + 1]):
                            # Next col is not empty
                            # Move the next col into current
                            board_changed = True
                            board[row_idx][col_idx] = board[row_idx][col_idx + 1]
                            board[row_idx][col_idx + 1] = " "
    elif direction == "up":
        while has_empty_between(board, direction):
            for row_idx, row in enumerate(board):
                if row_idx == 0:
                    # First row, skip
                    continue
                for col_idx, col in enumerate(row):
                    if is_empty(board[row_idx - 1][col_idx]):
                        # Col above empty
                        if not is_empty(col):
                            # Current col is not empty
                            # Move current col into above col
                            board_changed = True
                            board[row_idx - 1][col_idx] = board[row_idx][col_idx]
                            board[row_idx][col_idx] = " "
    elif direction == "down":
        while has_empty_between(board, direction):
            for row_idx, row in enumerate(board):
                if row_idx == len(board) - 1:
                    # Last row, skip
                    continue
                for col_idx, col in enumerate(row):
                    if is_empty(board[row_idx + 1][col_idx]):
                        # Col below empty
                        if not is_empty(col):
                            # Current col is not empty
                            # Move current col into col below
                            board_changed = True
                            board[row_idx + 1][col_idx] = board[row_idx][col_idx]
                            board[row_idx][col_idx] = " "
    return board_changed, board


def doKeyUp(board: Board) -> Tuple[bool, Board]:
    print("doKeyUp")

    # 1. COMPACT TILES
    board_changed, board = compact_tiles(board, "up")

    # 2. COMBINE TILES

    # cols_merged is a stylistic feature that prevents cascading merges
    # I'm not sure if the assignment requires this or not but the original
    # 2048 seems to operate this way.
    cols_merged = []

    for row_idx, row in enumerate(board):
        if row_idx == 0:
            # Skip if first row
            continue
        for col_idx, col in enumerate(row):
            if is_empty(board[row_idx - 1][col_idx]) or is_empty(board[row_idx][col_idx]):
                # Skip if one or the other is empty
                continue
            if board[row_idx - 1][col_idx] == board[row_idx][col_idx] and col_idx not in cols_merged:
                # Col above is same as current col
                # Merge col above into current col
                board_changed = True
                above_col_val = int(board[row_idx - 1][col_idx])
                current_col_val = above_col_val + int(board[row_idx][col_idx])
                board[row_idx][col_idx] = str(current_col_val)
                board[row_idx - 1][col_idx] = " "
                cols_merged.append(col_idx)

    # 3. COMPACT TILES
    if compact_tiles(board, "up")[0]:
        board_changed = True
    board = compact_tiles(board, "up")[1]

    return board_changed, board

# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Down' key.


def doKeyDown(board: Board) -> Tuple[bool, Board]:
    print("doKeyDown")

    # 1. COMPACT TILES
    board_changed, board = compact_tiles(board, "down")

    # 2. COMBINE TILES

    # cols_merged is a stylistic feature that prevents cascading merges
    # I'm not sure if the assignment requires this or not but the original
    # 2048 seems to operate this way.
    cols_merged = []

    for row_idx, row in enumerate(board):
        if row_idx == 0:
            # Skip if first row
            continue
        for col_idx, col in enumerate(row):
            if is_empty(board[row_idx - 1][col_idx]) or is_empty(board[row_idx][col_idx]):
                # Skip if one or the other is empty
                continue
            if board[row_idx - 1][col_idx] == board[row_idx][col_idx] and col_idx not in cols_merged:
                # Col above is same as current col
                # Merge col above into current col
                board_changed = True
                above_col_val = int(board[row_idx - 1][col_idx])
                current_col_val = above_col_val + int(board[row_idx][col_idx])
                board[row_idx][col_idx] = str(current_col_val)
                board[row_idx - 1][col_idx] = " "
                cols_merged.append(col_idx)

    # 3. COMPACT TILES
    if compact_tiles(board, "down")[0]:
        board_changed = True
    board = compact_tiles(board, "down")[1]

    return board_changed, board

# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Left' key.


def doKeyLeft(board: Board) -> Tuple[bool, Board]:
    print("doKeyLeft")

    # 1. COMPACT TILES
    board_changed, board = compact_tiles(board, "left")

    # 2. COMBINE TILES
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if col_idx == len(board[row_idx]) - 1:
                # Skip if last column
                continue
            if is_empty(board[row_idx][col_idx]) or is_empty(board[row_idx][col_idx + 1]):
                # Skip if one or the other is empty
                continue
            if board[row_idx][col_idx] == row[col_idx + 1]:
                # Current block is same as next block
                # Merge current block into next block
                board_changed = True
                current_block_val = int(board[row_idx][col_idx])
                next_block_val = current_block_val + int(board[row_idx][col_idx + 1])
                board[row_idx][col_idx] = " "
                board[row_idx][col_idx + 1] = str(next_block_val)

    # 3. COMPACT TILES
    if compact_tiles(board, "left")[0]:
        board_changed = True
    board = compact_tiles(board, "left")[1]

    return board_changed, board


# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Right' key.

def doKeyRight(board: Board) -> Tuple[bool, Board]:
    print("doKeyRight")

    # 1. COMPACT TILES
    board_changed, board = compact_tiles(board, "right")

    # 2. COMBINE TILES
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if col_idx == len(board[row_idx]) - 1:
                # Skip if last column
                continue
            if is_empty(board[row_idx][col_idx]) or is_empty(board[row_idx][col_idx + 1]):
                # Skip if one or the other is empty
                continue
            if board[row_idx][col_idx] == row[col_idx + 1]:
                # Current block is same as next block
                # Merge next block into current block
                board_changed = True
                next_block_val = int(board[row_idx][col_idx + 1])
                current_block_val = next_block_val + int(board[row_idx][col_idx])
                board[row_idx][col_idx] = str(current_block_val)
                board[row_idx][col_idx + 1] = " "

    # 3. COMPACT TILES
    if compact_tiles(board, "right")[0]:
        board_changed = True
    board = compact_tiles(board, "right")[1]

    return board_changed, board


# Returns a list of tuples (row, col)
# indicating where the empty spots are
def emptyPos(board: Board) -> List[Tuple[int, int]]:
    empty_positions = []
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if col == ' ': # is empty
                empty_positions.append((row_idx, col_idx))
    return empty_positions
