"""
    Given a square matrix mat, return the sum of the matrix diagonals.
    Only include the sum of all the elements on the primary diagonal and all 
    the elements on the secondary diagonal that are not part of the primary 
    diagonal.

    Example:
    Input: mat = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
    Output: 25
    Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
                 Notice that element mat[1][1] = 5 is counted only once.

    Example:
    Input: mat = [[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]]
    Output: 8

    Example:
    Input: mat = [[5]]
    Output: 5

    Constraints:
        - n == mat.length == mat[i].length
        - 1 <= n <= 100
        - 1 <= mat[i][j] <= 100
"""
#Difficulty: Easy
#113 / 113 test cases passed.
#Runtime: 100 ms
#Memory Usage: 14.3 MB

#Runtime: 100 ms, faster than 99.37% of Python3 online submissions for Matrix Diagonal Sum.
#Memory Usage: 14.3 MB, less than 5.09% of Python3 online submissions for Matrix Diagonal Sum.

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        length = len(mat)
        j = len(mat[0]) - 1
        for i in range(length):
            result += mat[i][i]
            if i != j:
                result += mat[i][j]
            j -= 1
        return result
