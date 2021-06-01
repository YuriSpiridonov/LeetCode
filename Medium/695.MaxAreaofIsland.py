'''
    You are given an m x n binary matrix grid. An island is 
    a group of 1's (representing land) connected 4-directionally 
    (horizontal or vertical.) You may assume all four edges 
    of the grid are surrounded by water.

    The area of an island is the number of cells with a value 
    1 in the island.

    Return the maximum area of an island in grid. If there 
    is no island, return 0.

    Example:
    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island 
                 must be connected 4-directionally.

    Example:
    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0

    Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m, n <= 50
        - grid[i][j] is either 0 or 1.
'''
#Difficulty: Medium
#728 / 728 test cases passed.
#Runtime: 160 ms
#Memory Usage: 16.3 MB

#Runtime: 160 ms, faster than 23.97% of Python3 online submissions for Max Area of Island.
#Memory Usage: 16.3 MB, less than 60.97% of Python3 online submissions for Max Area of Island.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxAreaOfIsland = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.area = 0
                    self.dfs(grid, i, j)
                    maxAreaOfIsland = max(maxAreaOfIsland, self.area)
        return maxAreaOfIsland

    def dfs(self, grid, row, col):
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[row]) - 1 or grid[row][col] == 0:
            return
        grid[row][col] = 0
        self.area += 1
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row + 1, col)
