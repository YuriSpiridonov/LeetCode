"""
    Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return 
    the number of special positions in mat.

    A position (i,j) is called special if mat[i][j] == 1 and all other elements 
    in row i and column j are 0 (rows and columns are 0-indexed).

    Example:
    Input: mat = [[1,0,0],
                  [0,0,1],
                  [1,0,0]]
    Output: 1
    Explanation: (1,2) is a special position because mat[1][2] == 1 and all 
                 other elements in row 1 and column 2 are 0.

    Example:
    Input: mat = [[1,0,0],
                  [0,1,0],
                  [0,0,1]]
    Output: 3
    Explanation: (0,0), (1,1) and (2,2) are special positions. 

    Example:
    Input: mat = [[0,0,0,1],
                  [1,0,0,0],
                  [0,1,1,0],
                  [0,0,0,0]]
    Output: 2

    Example:
    Input: mat = [[0,0,0,0,0],
                  [1,0,0,0,0],
                  [0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,1]]
    Output: 3

    Constraints:
        - rows == mat.length
        - cols == mat[i].length
        - 1 <= rows, cols <= 100
        - mat[i][j] is 0 or 1.
"""
#Difficulty: Easy
#95 / 95 test cases passed.
#Runtime: 220 ms
#Memory Usage: 13.9 MB

#Runtime: 220 ms, faster than 48.49% of Python3 online submissions for Special Positions in a Binary Matrix.
#Memory Usage: 13.9 MB, less than 61.78% of Python3 online submissions for Special Positions in a Binary Matrix.

class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        rows = len(mat)
        cols = len(mat[0])
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1 and self.rowCheck(mat, row) and self.colCheck(mat, rows, col):
                    count += 1
        return count

    def rowCheck(self, mat, row):
        return mat[row].count(1) == 1

    def colCheck(self, mat, rows, col):
        count = 0
        for row in range(rows):
            if mat[row][col] == 1:
                count += 1
        return count == 1
