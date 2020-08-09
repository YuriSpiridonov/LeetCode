"""
    In a given grid, each cell can have one of three values:
        - the value 0 representing an empty cell;
        - the value 1 representing a fresh orange;
        - the value 2 representing a rotten orange.
    Every minute, any fresh orange that is adjacent (4-directionally) to a 
    rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a 
    fresh orange. If this is impossible, return -1 instead.

    Example:
    Input: [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

    Example:
    Input: [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is 
                 never rotten, because rotting only happens 4-directiona

    Note:
        1. 1 <= grid.length <= 10
        2. 1 <= grid[0].length <= 10
        3. grid[i][j] is only 0, 1, or 2.
"""
#Difficulty: Medium
#303 / 303 test cases passed.
#Runtime: 52 ms
#Memory Usage: 13.7 MB

#Runtime: 52 ms, faster than 84.00% of Python3 online submissions for Rotting Oranges.
#Memory Usage: 13.7 MB, less than 91.03% of Python3 online submissions for Rotting Oranges.

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.rotten_value = 2
        self.rotting = True
        while self.rotting and self.checkForFreshOranges(grid):
            self.rotting = False
            for i in range(self.rows):
                for j in range(self.cols):
                    if grid[i][j] == self.rotten_value:
                        self.rottenOrange(grid, i - 1, j)
                        self.rottenOrange(grid, i, j - 1)
                        self.rottenOrange(grid, i, j + 1)
                        self.rottenOrange(grid, i + 1, j)
            if self.rotting:
                minutes += 1
                self.rotten_value += 1
        if not self.rotting:
            return -1
        return minutes

    def rottenOrange(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return
        if grid[i][j] == 1:
            grid[i][j] += self.rotten_value
            self.rotting = True

    def checkForFreshOranges(self, grid):
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    return True
        return False
