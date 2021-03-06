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
#Runtime: 148 ms
#Memory Usage: 14.7 MB
    
#Runtime: 148 ms, faster than 19.10% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
#Memory Usage: 14.7 MB, less than 66.55% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
        
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] < 0:
                    count += 1
        return count
