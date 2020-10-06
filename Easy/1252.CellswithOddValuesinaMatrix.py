"""
    Given n and m which are the dimensions of a matrix initialized by zeros and 
    given an array indices where indices[i] = [ri, ci]. For each pair of 
    [ri, ci] you have to increment all cells in row ri and column ci by 1.
    Return the number of cells with odd values in the matrix after applying the 
    increment to all indices.

    Example:
            [[0, 0, 0],  ->  [[1, 2, 1],  ->  [[1, 3, 1],
             [0, 0, 0]]       [0, 1, 0]]       [1, 3, 1]]
       
    Input: n = 2, m = 3, indices = [[0,1],[1,1]]
    Output: 6
    Explanation: Initial matrix = [[0,0,0],[0,0,0]].
                 After applying first increment it becomes [[1,2,1],[0,1,0]].
                 The final matrix will be [[1,3,1],[1,3,1]] which contains 6 
                 odd numbers.

    Example:
            [[0, 0],  ->  [[0, 1],  ->  [[2, 2],
             [0, 0]]       [1, 2]]       [2, 2]]

    Input: n = 2, m = 2, indices = [[1,1],[0,0]]
    Output: 0
    Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the 
                 final matrix.

    Constraints:
        - 1 <= n <= 50
        - 1 <= m <= 50
        - 1 <= indices.length <= 100
        - 0 <= indices[i][0] < n
        - 0 <= indices[i][1] < m
"""
#Difficulty: Easy
#44 / 44 test cases passed.
#Runtime: 44 ms
#Memory Usage: 14.2 MB

#Runtime: 44 ms, faster than 79.13% of Python3 online submissions for Cells with Odd Values in a Matrix.
#Memory Usage: 14.2 MB, less than 9.98% of Python3 online submissions for Cells with Odd Values in a Matrix.

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0 for j in range(m)] for i in range(n)]
        for row, col in indices:
            matrix[row] = [value + 1 for value in matrix[row]]
            for row in range(n):
                matrix[row][col] += 1
        return sum([1 if matrix[row][col] % 2 else 0 for row in range(n) for col in range(m)])
