"""
    Given a matrix of m x n elements (m rows, n columns), return all elements 
    of the matrix in spiral order.
    
    Example:
    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]
"""
#Difficulty: Medium
#22 / 22 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.9 MB

#Runtime: 28 ms, faster than 70.89% of Python3 online submissions for Spiral Matrix.
#Memory Usage: 13.9 MB, less than 8.70% of Python3 online submissions for Spiral Matrix.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return None
        rows = len(matrix)
        columns = len(matrix[0])
        row = 0
        col = 0
        count = 0
        result = list()
        go_reverse = False
        while count < columns * rows:
            if not go_reverse:
                while col < columns:
                    if matrix[row][col] is not None:
                        result.append(matrix[row][col])
                        matrix[row][col] = None
                        col += 1
                        count += 1
                    else:
                        break
                col -= 1
                if matrix[row][col] == None or col == columns:
                    row += 1
                while row < rows:
                    if matrix[row][col] is not None:
                        result.append(matrix[row][col])
                        matrix[row][col] = None
                        row += 1
                        count += 1
                    else:
                        break    
                row -= 1
                if matrix[row][col] == None or row == rows:
                    col -= 1
                go_reverse = not go_reverse
            else:
                while col > -1:
                    if matrix[row][col] is not None:
                        result.append(matrix[row][col])
                        matrix[row][col] = None
                        col -= 1
                        count += 1
                    else:
                        break
                if matrix[row][col] == None or col == -1:
                    col += 1
                    row -= 1
                while row > -1:
                    if matrix[row][col] is not None:
                        result.append(matrix[row][col])
                        matrix[row][col] = None
                        row -= 1
                        count += 1
                    else:
                        break
                if matrix[row][col] == None or row == -1:
                    col += 1
                    row += 1
                go_reverse = not go_reverse
        return result
