'''
    Given an m x n integers matrix, return the length of the 
    longest increasing path in matrix.

    From each cell, you can either move in four directions: 
    left, right, up, or down. You may not move diagonally or 
    move outside the boundary (i.e., wrap-around is not 
    allowed).

    Example:
    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].

    Example:
    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. 
                 Moving diagonally is not allowed.

    Example:
    Input: matrix = [[1]]
    Output: 1

    Constraints:
        - m == matrix.length
        - n == matrix[i].length
        - 1 <= m, n <= 200
        - 0 <= matrix[i][j] <= 2^31 - 1
'''
#Difficulty: Hard
#138 / 138 test cases passed.
#Runtime: 8376 ms
#Memory Usage: 544.7 MB

#Runtime: 8376 ms, faster than 5.01% of Python3 online submissions for Longest Increasing Path in a Matrix.
#Memory Usage: 544.7 MB, less than 5.07% of Python3 online submissions for Longest Increasing Path in a Matrix.

class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(i, j, 1)
        return self.res

    @lru_cache(None)
    def dfs(self, i, j, count):
        self.res = max(self.res, count)
        if i-1 >= 0 and self.matrix[i-1][j] > self.matrix[i][j]:
            self.dfs(i-1, j, count+1)
        if j-1 >= 0 and self.matrix[i][j-1] > self.matrix[i][j]:
            self.dfs(i, j-1, count+1)
        if i+1 < len(self.matrix) and self.matrix[i+1][j] > self.matrix[i][j]:
            self.dfs(i+1, j, count+1)
        if j+1 < len(self.matrix[0]) and self.matrix[i][j+1] > self.matrix[i][j]:
            self.dfs(i, j+1, count+1)
