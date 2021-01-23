'''
    A matrix diagonal is a diagonal line of cells starting 
    from some cell in either the topmost row or leftmost 
    column and going in the bottom-right direction until 
    reaching the matrix's end. For example, the matrix 
    diagonal starting from mat[2][0], where mat is a 6 x 3 
    matrix, includes cells mat[2][0], mat[3][1], and 
    mat[4][2].

    Given an m x n matrix mat of integers, sort each matrix 
    diagonal in ascending order and return the resulting 
    matrix.

    Example 1:
               [3,3,1,1]      [1,1,1,1]
               [2,2,1,2]  ->  [1,2,2,2]
               [1,1,1,2]      [1,2,3,3]

    Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

    Constraints:
        - m == mat.length
        - n == mat[i].length
        - 1 <= m, n <= 100
        - 1 <= mat[i][j] <= 100
'''
#Difficuty: Medium
#14 / 14 test cases passed.
#Runtime: 76 ms
#Memory Usage: 14.5 MB

#Runtime: 76 ms, faster than 96.55% of Python3 online submissions for Sort the Matrix Diagonally.
#Memory Usage: 14.5 MB, less than 90.66% of Python3 online submissions for Sort the Matrix Diagonally.

class Solution:

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.diagonalRowsCrawler(mat)
        return mat

    def diagonalRowsCrawler(self, mat: List[List[int]]) -> None:
        col = self.cols
        for row in range(self.rows):
            # iterate through diagonals on first row
            while col:
                col -= 1
                self.diagonalValueSort(mat, row, col)
            # iterate through diagonals on other rows
            self.diagonalValueSort(mat, row, col)

    def diagonalValueSort(self, mat: List[List[int]], row: int, col: int) -> None:
        diagonal_values = []
        # gather values
        while row < self.rows and col < self.cols:
            diagonal_values.append(mat[row][col])
            row += 1
            col += 1
        # sort values
        diagonal_values.sort()
        # replace current values with sorted
        while row > 0 and col > 0:
            row -= 1
            col -= 1
            mat[row][col] = diagonal_values.pop()