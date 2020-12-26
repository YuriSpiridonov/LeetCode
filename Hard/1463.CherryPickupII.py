'''
    Given a rows x cols matrix grid representing a field of 
    cherries. Each cell in grid represents the number of 
    cherries that you can collect.

    You have two robots that can collect cherries for you, 
    Robot #1 is located at the top-left corner (0,0) , and 
    Robot #2 is located at the top-right corner (0, cols-1) 
    of the grid.

    Return the maximum number of cherries collection using 
    both robots  by following the rules below:
        - From a cell (i,j), robots can move to cell 
          (i+1, j-1), (i+1, j) or (i+1, j+1).
        - When any robot is passing through a cell, It picks 
          it up all cherries, and the cell becomes an empty 
          cell (0).
        - When both robots stay on the same cell, only one 
          of them takes the cherries.
        - Both robots cannot move outside of the grid at any 
          moment.
        - Both robots should reach the bottom row in the grid.

    Example:
    Input: grid = [[3,1,1],
                   [2,5,1],
                   [1,5,5],
                   [2,1,1]]
    Output: 24
    Explanation: Path of robot #1 and #2 are described in 
                 color green and blue respectively.
                 Cherries taken by Robot #1, (3 + 2 + 5 + 2) 
                 = 12.
                 Cherries taken by Robot #2, (1 + 5 + 5 + 1) 
                 = 12.
                 Total of cherries: 12 + 12 = 24.

    Example:
    Input: grid = [[1,0,0,0,0,0,1],
                   [2,0,0,0,0,3,0],
                   [2,0,9,0,0,0,0],
                   [0,3,0,5,4,0,0],
                   [1,0,2,3,0,0,6]]
    Output: 28
    Explanation: Path of robot #1 and #2 are described in 
                 color green and blue respectively.
                 Cherries taken by Robot #1, (1 + 9 + 5 + 2) 
                 = 17.
                 Cherries taken by Robot #2, (1 + 3 + 4 + 3) 
                 = 11.
                 Total of cherries: 17 + 11 = 28.

    Example:
    Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
    Output: 22

    Example:
    Input: grid = [[1,1],[1,1]]
    Output: 4

    Constraints:
        - rows == grid.length
        - cols == grid[i].length
        - 2 <= rows, cols <= 70
        - 0 <= grid[i][j] <= 100 
'''
#Difficulty: Hard
#58 / 58 test cases passed.
#Runtime: 1024 ms
#Memory Usage: 54.6 MB

#Runtime: 1024 ms, faster than 68.56% of Python3 online submissions for Cherry Pickup II.
#Memory Usage: 54.6 MB, less than 5.28% of Python3 online submissions for Cherry Pickup II.

class Solution:

    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) 
        return self.dfs(0, 0, self.cols-1)

    @lru_cache(None)
    def dfs(self, row, x, y):
        if x < 0 or x >= self.cols or y < 0 or y >= self.cols:
            return 0
        result = 0
        result += self.grid[row][x]
        if x != y:
            result += self.grid[row][y]
        if row < self.rows - 1:
            vals = []
            for i in [x-1, x, x+1]:
                for j in [y-1, y, y+1]:
                    vals.append(self.dfs(row+1, i, j))
            result += max(vals)
        return result
