"""
    On an 8 x 8 chessboard, there is one white rook. There also may be empty 
    squares, white bishops, and black pawns.  These are given as characters 
    'R', '.', 'B', and 'p' respectively. Uppercase characters represent white 
    pieces, and lowercase characters represent black pieces.

    The rook moves as in the rules of Chess: it chooses one of four cardinal 
    directions (north, east, west, and south), then moves in that direction 
    until it chooses to stop, reaches the edge of the board, or captures an 
    opposite colored pawn by moving to the same square it occupies.  Also, 
    rooks cannot move into the same square as other friendly bishops.

    Return the number of pawns the rook can capture in one move.

    Example:
    Input: [[".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".","R",".",".",".","p"],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."]]
    Output: 3
    Explanation: 
                 In this example the rook is able to capture all the pawns.

    Example:
    Input: [[".",".",".",".",".",".",".","."],
            [".","p","p","p","p","p",".","."],
            [".","p","p","B","p","p",".","."],
            [".","p","B","R","B","p",".","."],
            [".","p","p","B","p","p",".","."],
            [".","p","p","p","p","p",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."]]
    Output: 0
    Explanation: 
                 Bishops are blocking the rook to capture any pawn.

    Example:
    Input: [[".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            ["p","p",".","R",".","p","B","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".","B",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".",".",".",".",".","."]]
    Output: 3
    Explanation: 
                 The rook can capture the pawns at positions b5, d6 and f5.

    Note:
        1. board.length == board[i].length == 8
        2. board[i][j] is either 'R', '.', 'B', or 'p'
        3. There is exactly one cell with board[i][j] == 'R'
"""
#Difficulty: Easy
#22 / 22 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14.2 MB

#Runtime: 40 ms, faster than 6.85% of Python3 online submissions for Available Captures for Rook.
#Memory Usage: 14.1 MB, less than 44.63% of Python3 online submissions for Available Captures for Rook.

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        pawns = 0
        for i in range(8):
            if 'R' in board[i]:
                j = board[i].index('R')
                vert = [board[i][j] for i in range(8)]
                pawns += self.counter(board[i][:j][::-1])
                pawns += self.counter(board[i][j+1:])
                pawns += self.counter(vert[:i][::-1])
                pawns += self.counter(vert[i+1:])
                break
        return pawns

    def counter(self, line):
        for char in line:
            if char == 'p':
                return 1
            if char == 'B':
                break
        return 0
