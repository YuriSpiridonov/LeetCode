'''
    According to Wikipedia's article: "The Game of Life, also 
    known simply as Life, is a cellular automaton devised by 
    the British mathematician John Horton Conway in 1970."

    The board is made up of an m x n grid of cells, where 
    each cell has an initial state: live (represented by a 1) 
    or dead (represented by a 0). Each cell interacts with 
    its eight neighbors (horizontal, vertical, diagonal) 
    using the following four rules (taken from the above 
    Wikipedia article):
        1. Any live cell with fewer than two live neighbors 
           dies as if caused by under-population.
        2. Any live cell with two or three live neighbors 
           lives on to the next generation.
        3. Any live cell with more than three live neighbors 
           dies, as if by over-population.
        4. Any dead cell with exactly three live neighbors 
           becomes a live cell, as if by reproduction.

    The next state is created by applying the above rules 
    simultaneously to every cell in the current state, where 
    births and deaths occur simultaneously. Given the current 
    state of the m x n grid board, return the next state.

    Example:
    Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

    Example:
    Input: board = [[1,1],[1,0]]
    Output: [[1,1],[1,1]]

    Constraints:
        - m == board.length
        - n == board[i].length
        - 1 <= m, n <= 25
        - board[i][j] is 0 or 1.

    Follow up:
        - Could you solve it in-place? Remember that the 
          board needs to be updated simultaneously: You 
          cannot update some cells first and then use their 
          updated values to update other cells.
        - In this question, we represent the board using a 
          2D array. In principle, the board is infinite, 
          which would cause problems when the active area 
          encroaches upon the border of the array (i.e., 
          live cells reach the border). How would you 
          address these problems?
'''
#Difficulty: Medium
#22 / 22 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14.4 MB

#Runtime: 36 ms, faster than 43.17% of Python3 online submissions for Game of Life.
#Memory Usage: 14.4 MB, less than 27.97% of Python3 online submissions for Game of Life.

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                board[i][j] = [board[i][j], 0]

        for i in range(rows):
            for j in range(cols):
                neighbors = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == y == 0:
                            continue
                        else:
                            if 0 <= i+x < rows and 0 <= j+y < cols:
                                neighbors += board[i+x][j+y][0]
                if board[i][j][0] == 1:
                    board[i][j][1] = 0 if neighbors not in [2, 3] else 1
                else:
                    board[i][j][1] = 1 if neighbors == 3 else 0

        for i in range(rows):
            for j in range(cols):
                board[i][j] = board[i][j][1]
