"""
    Given a m * n matrix of distinct numbers, return all lucky numbers in the 
    matrix in any order.
    A lucky number is an element of the matrix such that it is the minimum 
    element in its row and maximum in its column.

    Example:
    Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
    Output: [15]
    Explanation: 15 is the only lucky number since it is the minimum in its row 
                 and the maximum in its column

    Example:
    Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    Output: [12]
    Explanation: 12 is the only lucky number since it is the minimum in its row 
                 and the maximum in its column.

    Constraints:
        - m == mat.length
        - n == mat[i].length
        - 1 <= n, m <= 50
        - 1 <= matrix[i][j] <= 10^5.
        - All elements in the matrix are distinct.
"""
#Difficulty: Easy
#103 / 103 test cases passed.
#Runtime: 132 ms
#Memory Usage: 14.2 MB

#Runtime: 132 ms, faster than 92.30% of Python3 online submissions for Lucky Numbers in a Matrix.
#Memory Usage: 14.2 MB, less than 25.20% of Python3 online submissions for Lucky Numbers in a Matrix.

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky = []
        rows = len(matrix)
        cols = len(matrix[0])
        for col in range(cols):
            maximum = matrix[0][col]
            max_row = 0
            for row in range(rows):
                if matrix[row][col] > maximum:
                    maximum = matrix[row][col]
                    max_row = row
            if maximum == min(matrix[max_row]):
                lucky.append(maximum)
        return lucky
