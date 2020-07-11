"""
    Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be 
    validated according to the following rules:
        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 
           without repetition.

    A partially filled sudoku which is valid.
    The Sudoku board could be partially filled, where empty cells are filled 
    with the character '.'.

    Example:
    Input:
    [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner 
                 being modified to 8. Since there are two 8's in the top left 
                 3x3 sub-box, it is invalid.
    Note:
        - A Sudoku board (partially filled) could be valid but is not 
          necessarily solvable.
        - Only the filled cells need to be validated according to the mentioned 
          rules.
        - The given board contain only digits 1-9 and the character '.'.
        - The given board size is always 9x9.
"""
#Difficulty: Medium
#504 / 504 test cases passed.
#Runtime: 104 ms
#Memory Usage: 13.9 MB

#Runtime: 104 ms, faster than 61.02% of Python3 online submissions for Valid Sudoku.
#Memory Usage: 13.9 MB, less than 32.72% of Python3 online submissions for Valid Sudoku.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        squares = [[], [], []]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and board[i][j] not in row:
                    row.add(board[i][j])
                elif board[i][j] in row:
                    return False
                if board[j][i] != '.' and board[j][i] not in col:
                    col.add(board[j][i])
                elif board[j][i] in col:
                    return False
            row = set()
            col = set()
        for step in range(0,9,3):
            for i in range(9):
                squares[0] += board[i][0:3]
                squares[1] += board[i][3:6]
                squares[2] += board[i][6:9]
                if len(squares[0]) == 9:
                    for square in squares:
                        if not self.squareCheck(square):
                            return False
                    squares = [[], [], []]
        return True

    def squareCheck(self, s):
        square = set()
        for n in s:
            if n != '.' and n not in square:
                square.add(n)
            elif n in square:
                return False
        return True
