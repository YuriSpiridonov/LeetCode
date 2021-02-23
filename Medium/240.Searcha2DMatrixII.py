'''
    Write an efficient algorithm that searches for a target 
    value in an m x n integer matrix. The matrix has the 
    following properties:
        - Integers in each row are sorted in ascending from 
          left to right.
        - Integers in each column are sorted in ascending 
          from top to bottom.

    Example:
    Input: matrix = [[1,4,7,11,15],
                    [2,5,8,12,19],
                    [3,6,9,16,22],
                    [10,13,14,17,24],
                    [18,21,23,26,30]], 
        target = 5
    Output: true

    Example:
    Input: matrix = [[1,4,7,11,15],
                    [2,5,8,12,19],
                    [3,6,9,16,22],
                    [10,13,14,17,24],
                    [18,21,23,26,30]], 
        target = 20
    Output: false

    Constraints:
        - m == matrix.length
        - n == matrix[i].length
        - 1 <= n, m <= 300
        - -10^9 <= matix[i][j] <= 10^9
        - All the integers in each row are sorted in 
          ascending order.
        - All the integers in each column are sorted in 
          ascending order.
        - -10^9 <= target <= 10^9
'''
#Difficulty: Medium
#128 / 128 test cases passed.
#Runtime: 168 ms
#Memory Usage: 20.4 MB

#Runtime: 168 ms, faster than 52.23% of Python3 online submissions for Search a 2D Matrix II.
#Memory Usage: 20.4 MB, less than 98.26% of Python3 online submissions for Search a 2D Matrix II.

class Solution:

    def searchMatrix(self, matrix, target):
        target_in_matrix = False
        if not matrix or not matrix[0]:
            return False
        for row in matrix:
            target_in_matrix = self.binarySearch(row, target)
            if target_in_matrix:
                break
        return target_in_matrix

    def binarySearch(self, row, target):
        l = 0
        r = len(row) - 1
        while l <= r:
            m = (l+r) // 2
            if row[m] == target:
                return True
            if row[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
