'''
    A robot is located at the top-left corner of a m x n grid 
    (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point 
    in time. The robot is trying to reach the bottom-right 
    corner of the grid (marked 'Finish' in the diagram below).

    Now consider if some obstacles are added to the grids. 
    How many unique paths would there be?

    An obstacle and space is marked as 1 and 0 respectively 
    in the grid.

    Example:
    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: There is one obstacle in the middle of the 
                 3x3 grid above.
                 There are two ways to reach the bottom-right 
                 corner:
                 1. Right -> Right -> Down -> Down
                 2. Down -> Down -> Right -> Right

    Example:
    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1

    Constraints:
        - m == obstacleGrid.length
        - n == obstacleGrid[i].length
        - 1 <= m, n <= 100
        - obstacleGrid[i][j] is 0 or 1.
'''
#Difficulty: Medium
#41 / 41 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14.1 MB

#Runtime: 40 ms, faster than 78.35% of Python3 online submissions for Unique Paths II.
#Memory Usage: 14.1 MB, less than 94.59% of Python3 online submissions for Unique Paths II.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # count paths in the first row
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j] != 1:
                if j == 0:
                    obstacleGrid[0][j] = 1
                else:
                    obstacleGrid[0][j] += obstacleGrid[0][j-1]
            else:
                obstacleGrid[0][j] = 0

        # count paths in the rest of the matrix
        for i in range(1, len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if  obstacleGrid[i][j] != 1:
                    if j != 0:
                        obstacleGrid[i][j] += (obstacleGrid[i][j-1] + obstacleGrid[i-1][j])
                    else:
                        obstacleGrid[i][j] += obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]