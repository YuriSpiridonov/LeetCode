"""
    Write an efficient algorithm that searches for a value in an m x n matrix. 
    This matrix has the following properties:
    - Integers in each row are sorted from left to right.
    - The first integer of each row is greater than the last integer of the 
      previous row.
    
    Example:
    Input:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    Output: true
"""
#Difficulty: Medium
#136 / 136 test cases passed.
#Runtime: 64 ms
#Memory Usage: 15.9 MB

#Runtime: 64 ms, faster than 84.49% of Python3 online submissions for Search a 2D Matrix.
#Memory Usage: 15.9 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix

class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return
        self.rows = len(matrix) - 1
        self.cols = len(matrix[0]) - 1
        return self.binarySearchRow(0, self.rows, matrix, target)
        
    def binarySearchRow(self, left, right, matrix, target):
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.binarySearchTarget(0, self.cols, matrix[mid], target)
            if matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
                
    def binarySearchTarget(self, left, right, matrix, target):
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid] == target:
                return True
            if matrix[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
