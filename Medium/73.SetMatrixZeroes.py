"""
    Given a m x n matrix, if an element is 0, set its entire row and column 
    to 0. Do it in-place.

    Example:
    Input: 
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    Output: 
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]
    Follow up:
        - A straight forward solution using O(mn) space is probably a bad idea.
        - A simple improvement uses O(m + n) space, but still not the best 
          solution.
        - Could you devise a constant space solution?
"""
#Diffculty: Medium
#159 / 159 test cases passed.
#Runtime: 128 ms
#Memory Usage: 14.2 MB

#Runtime: 128 ms, faster than 98.17% of Python3 online submissions for Set Matrix Zeroes.
#Memory Usage: 14.2 MB, less than 66.80% of Python3 online submissions for Set Matrix Zeroes.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_size = len(matrix[0])
        col_size = len(matrix)
        rows_to_zero = set()
        cols_to_zero = set()
        for i in range(col_size):
            for j in range(row_size):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)
        for i in range(col_size):
            if i in rows_to_zero:
                matrix[i] = [0] * row_size
            for j in cols_to_zero:
                matrix[i][j] = 0
