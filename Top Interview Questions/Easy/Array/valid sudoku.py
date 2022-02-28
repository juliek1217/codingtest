# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = 9
        for i in range(l):
            # check row
            gr = (board[r][i] for r in range(l) if board[r][i] != '.')
            # Python Counter takes in input a list, tuple, dictionary, string, which are all iterable objects, and it will give you output that will have the count of each element.
            if any(v != 1 for v in Counter(gr).values()):
                return False
            # check col
            gc = (board[i][c] for c in range(l) if board[i][c] != '.')
            if any(v != 1 for v in Counter(gc).values()):
                return False
        # check subboxes
        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                g = (board[i][j] for i in range(y, y+3)
                     for j in range(x, x+3) if board[i][j] != '.')
                if any(v != 1 for v in Counter(g).values()):
                    return False
        return True
