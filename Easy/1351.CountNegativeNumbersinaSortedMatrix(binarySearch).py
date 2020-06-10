"""
    Given a m * n matrix grid which is sorted in non-increasing order both 
    row-wise and column-wise. 
    Return the number of negative numbers in grid.
    
    Example:
    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8
    Explanation: There are 8 negatives number in the matrix.
    
    Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m, n <= 100
        - -100 <= grid[i][j] <= 100
"""
#Difficulty: Easy
#44 / 44 test cases passed.
#Runtime: 128 ms
#Memory Usage: 14.8 MB

#Runtime: 128 ms, faster than 63.80% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
#Memory Usage: 14.8 MB, less than 40.58% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            count += len(row[self.binarySearch(row):])
        return count

    def binarySearch(self, row):
        left = 0
        right = len(row) - 1
        while left <= right:
            middle = (left + right) // 2
            if row[middle] < 0 and row[middle-1] >= 0:
                return middle
            if row[middle] < 0 and row[middle-1] <= 0:
                right = middle - 1
            else:
                left = middle + 1
        return right + 1
