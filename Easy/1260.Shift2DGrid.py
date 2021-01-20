'''
    Given a 2D grid of size m x n and an integer k. You need 
    to shift the grid k times.

    In one shift operation:
        - Element at grid[i][j] moves to grid[i][j + 1].
        - Element at grid[i][n - 1] moves to grid[i + 1][0].
        - Element at grid[m - 1][n - 1] moves to grid[0][0].

    Return the 2D grid after applying shift operation k times.

    Example:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[9,1,2],[3,4,5],[6,7,8]]

    Example:
    Input: grid = [[3,8,1,9],
                   [19,7,2,5],
                   [4,6,11,10],
                   [12,0,21,13]], 
           k = 4
    Output: [[12,0,21,13],
             [3,8,1,9],
             [19,7,2,5],
             [4,6,11,10]]

    Example:
    Input: grid = [[1,2,3],
                   [4,5,6],
                   [7,8,9]], 
           k = 9
    Output: [[1,2,3],
             [4,5,6],
             [7,8,9]]

    Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m <= 50
        - 1 <= n <= 50
        - -1000 <= grid[i][j] <= 1000
        - 0 <= k <= 100
'''
#Difficulty: Easy
#107 / 107 test cases passed.
#Runtime: 148 ms
#Memory Usage: 14.8 MB

#Runtime: 148 ms, faster than 95.38% of Python3 online submissions for Shift 2D Grid.
#Memory Usage: 14.8 MB, less than 14.07% of Python3 online submissions for Shift 2D Grid.

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        j = 0
        cols = len(grid[0])
        rows = len(grid)
        k %= cols*rows # if k > matrix length
        vector = []

        # construct vector
        for row in grid:
            vector.extend(row)
        # shift values
        vector = vector[-k:] + vector[:-k]

        #re construct matrix
        for i in range(rows):
            grid[i] = vector[j:j+cols]
            j += cols

        return grid