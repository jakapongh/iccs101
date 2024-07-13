def get_diagonals(grid: list[str]) -> list[list[str]]:
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

    # Traverse from top right to bottom left
    """
        x are items that will be checked

        - - - - - - - x           x x x x x x x x
        - - - - - - x x           x x x x x x x -
        - - - - - x x x           x x x x x x - -
        - - - - x x x x           x x x x x - - -
        - - - x x x x x           x x x x - - - -
        - - x x x x x x           x x x - - - - -
        - x x x x x x x           x x - - - - - -
        x x x x x x x x           x - - - - - - -
    """
    rows = len(grid)
    cols = len(grid[0])
    for main_row in range(rows + cols - 1):
        new_row = []
        for row_idx in range(rows - 1, -1, -1):
            pos = main_row - row_idx
            if 0 <= pos < cols:
                char = grid[row_idx][pos]
                new_row.append(char)
        grid_diagonal.append(new_row)


    return grid_diagonal

def findWinner(B: list[str]) -> str:
    # ===================================================================
    # Check winners horizontally
    for row in B:
        current_player = None
        current_count = 0
        for col in row:
            if col == '.':
                current_player = None
                current_count = 0
                continue
            if current_player is None:
                # Hasn't been initialised yet
                current_player = col
                current_count = 1
            else:
                # Has already been initialised
                if current_player != col:
                    # Current slot is not the same as last slot, reset count
                    current_player = col
                    current_count = 1
                else:
                    # Current slot is the same as last slot, increment count
                    current_count += 1

            # Return winner if has winner
            if current_count >= 4:
                print('Returning', current_player, 'horizontal')
                return current_player

    # ===================================================================
    # Check winners vertically
    height_of_board = len(B)
    length_of_board = len(B[0])
    for col_idx in range(length_of_board):
        current_player = None
        current_count = 0
        for row_idx in range(height_of_board):
            row = B[row_idx][col_idx]
            if row == '.':
                current_player = None
                current_count = 0
                continue
            if current_player is None:
                # Hasn't been initialised yet
                current_player = row
                current_count = 1
            else:
                # Has already been initialised
                if current_player != row:
                    # Current slot is not the same as last slot, reset count
                    current_player = row
                    current_count = 1
                else:
                    # Current slot is the same as last slot, increment count
                    current_count += 1

            # Return winner if has winner
            if current_count >= 4:
                print('Returning', current_player, 'vertical')
                return current_player

    # ===================================================================
    # Check winners diagonally
    diagonals = get_diagonals(B)
    for diagonal in diagonals:
        current_player = None
        current_count = 0
        for col in diagonal:
            if col == '.':
                current_player = None
                current_count = 0
                continue

            if current_player is None:
                # Hasn't been initialised yet
                current_player = col
                current_count = 1
            else:
                # Has already been initialised
                if current_player != col:
                    # Current slot is not the same as last slot, reset count
                    current_player = col
                    current_count = 1
                else:
                    # Current slot is the same as last slot, increment count
                    current_count += 1

            # Return winner if has winner
            if current_count >= 4:
                print('Returning', current_player, 'diagonal')
                return current_player

    print('Returning - end case')
    return '-'


def test_findWinner():
    # # LTR Test
    # assert (findWinner(['RRRG', '....', 'GRRG', '.R..']) == '-')
    #
    # # Vertical test
    # assert (findWinner(['RRRG', 'R...', 'RRRG', 'RR..']) == 'R')
    #
    # # Diagonal test
    # assert (findWinner(['GRRG', '.GGR', 'GRGR', 'RGRG']) == 'G')
    #
    ### Winner ###
    assert (findWinner(['RRRG', '....', 'GRRG', '.R..']) == '-')
    assert (findWinner(['GRRG', '.GGR', 'GRGR', 'RGRG']) == 'G')
    assert (findWinner(['RG..', '....', '....', 'RGR.']) == '-')
    assert (findWinner(['RRGG', 'RGRG', 'GR.R', 'GRRG']) == '-')
    assert (findWinner(['GR..', '.G..', '..G.', '...G']) == 'G')
    assert (findWinner(['GRG.', '.GGG', 'GGGG', 'GGGG']) == 'G')
    assert (findWinner(['..RG', '..R.', '..G.', '..G.']) == '-')
    assert (findWinner(['R..R', 'RG.R', 'G.GG', '.RRG']) == '-')
    assert (findWinner(['R...', '..R.', 'RGG.', '....']) == '-')
    assert (findWinner(['RRRR', 'R.R.', 'GRGR', '.GRG']) == 'R')
    assert (findWinner(['G..R', '....', '...R', '..GR']) == '-')
    assert (findWinner(['GGGR', 'RRGR', 'RRRG', 'GG.G']) == '-')
    assert (findWinner(['G.R.', '.G..', 'G...', '..R.']) == '-')
    assert (findWinner(['GRGR', 'RRR.', 'GRG.', 'GGGG']) == 'G')
    assert (findWinner(['RR..G', 'G....', '.G...', 'R.G..', '.....']) == '-')
    assert (findWinner(['GRGR.', 'R.RRR', 'R...R', 'GGGR.', 'GGRRG']) == '-')
    assert (findWinner(['.GR..', 'RG...', 'GG.G.', 'RG.R.', '....G']) == 'G')
    assert (findWinner(['GG.RG', 'GGRGG', 'GRG..', 'GGRGG', '.RRGR']) == 'G')
    assert (findWinner(['..R..', '.GR.R', '.....', '..GG.', '.....']) == '-')
    assert (findWinner(['RR..R', '.GRRG', '..RG.', 'RRGG.', '.RRRG']) == 'R')
    assert (findWinner(['R..RG', 'RR..R', '.....', '.....', '.R...']) == '-')
    assert (findWinner(['RGR.G', 'RRRRR', 'RR.RR', 'GRG.R', 'GR.RG']) == 'R')
    assert (findWinner(['.....', 'GG...', 'G..G.', '.R...', '....R']) == '-')
    assert (findWinner(['RRR.R', 'GGGGR', 'GGGRR', 'GRGGG', 'RG..G']) == 'G')
    assert (findWinner(['...RG', '...R.', '.....', '....R', '.G..G']) == '-')
    assert (findWinner(['R.G..', 'GGGGG', 'G.GRG', 'GRRG.', 'GR.GG']) == 'G')
    assert (findWinner(['G..RR.', '......', '..R.G.', '.G.RRR', '.RG.R.', '.....R']) == 'R')
    assert (findWinner(['RGGGRG', '.RRGR.', 'RRGR..', 'GGRGRG', '.RGG.G', 'G.R.R.']) == 'R')
    assert (findWinner(['......', 'GG....', 'G.....', 'GG....', 'GR....', '..G...']) == 'G')
    assert (findWinner(['G.GG.G', 'GGR..G', 'GRRGR.', 'G.RGG.', '..GGR.', 'GRGGGG']) == 'G')
    assert (findWinner(['GRR..G', 'R.R...', '....R.', '......', '...R..', 'GG....']) == '-')
    assert (findWinner(['GRRRGG', 'RGR.R.', 'G.RRGR', 'G.GRRG', 'GRRGGR', '..RRGR']) == 'R')
    assert (findWinner(['R.....', 'R.R...', '.G.GR.', '...R..', 'G.G...', '......']) == '-')
    assert (findWinner(['.GGGGR', 'RGGRRG', 'RR...R', 'GR.GG.', '.G.RRG', 'R.GGRG']) == 'G')
    assert (findWinner(['G..G.R', '..G...', '....G.', '.....G', 'R.R...', '......']) == '-')
    assert (findWinner(['GGGG..', 'GRGRRR', 'G.GGGG', 'GGRRGG', 'GGGGGG', 'GR..RG']) == 'G')
    assert (findWinner(['R.R...', '...R.G', '.R....', 'RR....', '......', '.GGR..']) == '-')
    assert (findWinner(['GRGG..', 'G..GRG', 'GRRR.R', '..GRGR', '.GG.RR', '.GG.RR']) == 'R')
    assert (findWinner(['..RR...', '.G..R..', '.......', '...RG..', '..R..G.', 'RR.R..R', 'R......']) == 'R')
    assert (findWinner(['GRRG...', 'RRRGRRR', 'GGGRRG.', '.GGRGRR', 'G..GRRR', 'RRR.RRR', 'RRGGR.G']) == 'G')
    assert (findWinner(['...G.G.', '..G..R.', '....G..', '....R.G', '...R..G', '....R..', '.....R.']) == '-')
    assert (findWinner(['.GRRRG.', 'GR..RRG', 'GRGGRG.', 'GGGGGRR', 'R.GRGGG', '.RGR.GG', 'RRGGRGR']) == 'G')
    assert (findWinner(['G..RG..', '.......', '.R.....', '.......', '......R', '.......', '.....G.']) == '-')
    assert (findWinner(['GGRRGGR', 'RGGRR.R', 'RRG..GR', 'R.GG.GG', 'GR.GR.R', 'R.G..RR', 'RG.G..G']) == 'G')
    assert (findWinner(['..G.GR.', '..R....', '.......', 'G.R.RR.', '.R..R.G', 'R.G....', 'R.G....']) == '-')
    assert (findWinner(['GRRRRGG', 'RRRRGRG', 'RGGRGGR', 'RGGGRRR', 'G.RGGGR', '..GRR.R', 'GGRR.GR']) == 'R')
    assert (findWinner(['...GG..', '...G...', 'R..G.G.', '..RG.R.', '.......', '..RR...', '..R.R..']) == 'G')
    assert (findWinner(['GGR.RR.', 'R.GRGRR', '.GGGGR.', 'RGGG.GR', 'RGGGGRR', 'G.GRGGR', 'GRG.RGG']) == 'G')
    assert (findWinner(['....R..', 'G...R..', '.......', 'GR.....', '..G....', '......R', '..RG.R.']) == '-')
    assert (findWinner(['GRRR.R.', 'GGRRRGR', 'GRRR.GG', 'RRGGG.R', 'GGG.RGG', '.GR..GR', 'RRGGRGR']) == 'R')


test_findWinner()
