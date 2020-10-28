"""
    Given a 2D matrix matrix, find the sum of the elements inside the rectangle 
    defined by its upper left corner (row1, col1) and lower right corner 
    (row2, col2).

    Range Sum Query 2D
    [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, [2, 0, 1,] 5],
      [4, [1, 0, 1,] 7],
      [1, [0, 3, 0,] 5]
    ]
    The above rectangle (with the red border) is defined by 
    (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

    Example:
    Given matrix = [
                      [3, 0, 1, 4, 2],
                      [5, 6, 3, 2, 1],
                      [1, 2, 0, 1, 5],
                      [4, 1, 0, 1, 7],
                      [1, 0, 3, 0, 5]
                   ]

    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12

    Note:
        1. You may assume that the matrix does not change.
        2. There are many calls to sumRegion function.
        3. You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
#Difficulty: Medium
#12 / 12 test cases passed.
#Runtime: 1032 ms
#Memory Usage: 16.3 MB

#Runtime: 1032 ms, faster than 20.82% of Python3 online submissions for Range Sum Query 2D - Immutable.
#Memory Usage: 16.3 MB, less than 6.03% of Python3 online submissions for Range Sum Query 2D - Immutable.
  
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sum = 0
        for row in matrix:
            self.sum += sum(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix_sum = self.sum
        for i in range(len(self.matrix)):
            if i not in range(row1, row2+1):
                matrix_sum -= sum(self.matrix[i])
            else:
                matrix_sum -= sum(self.matrix[i][:col1])
                matrix_sum -= sum(self.matrix[i][col2+1:])
        return matrix_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
