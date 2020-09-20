"""
    On a 2-dimensional grid, there are 4 types of squares:
        - 1 represents the starting square.  There is exactly one starting 
          square.
        - 2 represents the ending square.  There is exactly one ending square.
        - 0 represents empty squares we can walk over.
        - -1 represents obstacles that we cannot walk over.
    Return the number of 4-directional walks from the starting square to the 
    ending square, that walk over every non-obstacle square exactly once.

    Example:
    Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    Output: 2
    Explanation: We have the following two paths: 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

    Example:
    Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    Output: 4
    Explanation: We have the following four paths: 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
    2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
    3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
    4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

    Example:
    Input: [[0,1],[2,0]]
    Output: 0
    Explanation: 
    There is no path that walks over every empty square exactly once.
    Note that the starting and ending square can be anywhere in the grid.

    Note:
        1. 1 <= grid.length * grid[0].length <= 20
"""
#Difficulty: Hard
#39 / 39 test cases passed.
#Runtime: 44 ms
#Memory Usage: 14 MB

#Runtime: 44 ms, faster than 99.30% of Python3 online submissions for Unique Paths III.
#Memory Usage: 14 MB, less than 19.04% of Python3 online submissions for Unique Paths III.

class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.steps = 0
        self.result = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 0:
                    self.steps += 1
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    self.dfs(row + 1, col)
                    self.dfs(row - 1, col)
                    self.dfs(row, col + 1)
                    self.dfs(row, col - 1)
        return self.result

    def dfs(self, row, col, steps_count = 0):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.grid[row][col] == -1:
            return
        elif self.grid[row][col] == 2 and steps_count == self.steps:
            self.result += 1
        elif self.grid[row][col] == 0:
            self.grid[row][col] = -1
            self.dfs(row + 1, col, steps_count + 1)
            self.dfs(row - 1, col, steps_count + 1)
            self.dfs(row, col + 1, steps_count + 1)
            self.dfs(row, col - 1, steps_count + 1)
            self.grid[row][col] = 0
