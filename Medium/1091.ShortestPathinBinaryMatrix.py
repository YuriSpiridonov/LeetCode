'''
    In an N by N square grid, each cell is either empty (0) 
    or blocked (1).

    A clear path from top-left to bottom-right has length k 
    if and only if it is composed of cells C_1, C_2, ..., 
    C_k such that:

        - Adjacent cells C_i and C_{i+1} are connected 
          8-directionally (ie., they are different and share 
          an edge or corner)
        - C_1 is at location (0, 0) (ie. has value grid[0][0])
        - C_k is at location (N-1, N-1) (ie. has value 
          grid[N-1][N-1])
        - If C_i is located at (r, c), then grid[r][c] is 
          empty (ie. grid[r][c] == 0).

    Return the length of the shortest such clear path from 
    top-left to bottom-right.  If such a path does not exist, 
    return -1.

    Example:
    Input: [[0,1],[1,0]]
    Output: 2

    Example:
    Input: [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4

    Note:
        1. 1 <= grid.length == grid[0].length <= 100
        2. grid[r][c] is 0 or 1
'''
#Difficulty: Medium
#84 / 84 test cases passed.
#Runtime: 1252 ms
#Memory Usage: 14.6 MB

#Runtime: 1252 ms, faster than 5.49% of Python3 online submissions for Shortest Path in Binary Matrix.
#Memory Usage: 14.6 MB, less than 90.70% of Python3 online submissions for Shortest Path in Binary Matrix.

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid) - 1
        if grid[0][0] == 1 or grid[rows][rows] == 1:
            return -1
        steps = 0
        queue = [(0, 0)]
        while queue:
            steps += 1
            length = len(queue)
            while length:
                length -= 1
                x, y = queue.pop(0)
                if grid[x][y] == 0:
                    grid[x][y] = 1
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if x+dx in range(0, rows+1) and y+dy in range(0, rows+1) and grid[x+dx][y+dy] == 0:
                                queue.append((x+dx, y+dy))
                if x == y == rows:
                    return steps
        return -1