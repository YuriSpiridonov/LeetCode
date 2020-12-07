"""
    Given a positive integer n, generate an n x n matrix filled with elements 
    from 1 to n^2 in spiral order.

    Example:
    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]

    Example:
    Input: n = 1
    Output: [[1]]

    Constraints:
        - 1 <= n <= 20
"""
#Difficulty: Medium
#20 / 20 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.4 MB

#Runtime: 28 ms, faster than 84.67% of Python3 online submissions for Spiral Matrix II.
#Memory Usage: 14.4 MB, less than 26.01% of Python3 online submissions for Spiral Matrix II.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row = 0
        col = 0
        val = 1
        matrix = [[None for i in range(n)] for j in range(n)]
        reverse = False
        while val <= n**2:
            if not reverse:
                while col < n:
                    if matrix[row][col] is None:
                        matrix[row][col] = val
                        col += 1
                        val += 1
                    else:
                        break
                col -= 1
                if matrix[row][col] is not None or col == n:
                    row += 1
                while row < n:
                    if matrix[row][col] is None:
                        matrix[row][col] = val
                        row += 1
                        val += 1
                    else:
                        break
                row -= 1
                if matrix[row][col] is not None or row == n:
                    col -= 1
                reverse = not reverse
            else:
                while col >= 0:
                    if matrix[row][col] is None:
                        matrix[row][col] = val
                        col -= 1
                        val += 1
                    else:
                        break
                if matrix[row][col] is not None or col < 0:
                    col += 1
                    row -= 1
                while row >= 0:
                    if matrix[row][col] is None:
                        matrix[row][col] = val
                        row -= 1
                        val += 1
                    else:
                        break
                if matrix[row][col] is not None or row < 0:
                    col += 1
                    row += 1
                reverse = not reverse
        return matrix
