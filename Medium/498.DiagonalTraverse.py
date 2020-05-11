"""
    Given a matrix of M x N elements (M rows, N columns), return all elements 
    of the matrix in diagonal order as shown in the below image.
    
    Example:
    Input:
    [ [ 1, 2, 3 ],
      [ 4, 5, 6 ],
      [ 7, 8, 9 ] ]
    Output:  [1,2,4,7,5,3,6,8,9]
    
    Theory:
    https://www.geeksforgeeks.org/print-matrix-diagonal-pattern/
"""
#Difficulty: Medium
#32 / 32 test cases passed.
#Runtime: 212 ms
#Memory Usage: 16.3 MB

#Runtime: 212 ms, faster than 52.29% of Python3 online submissions for Diagonal Traverse.
#Memory Usage: 16.3 MB, less than 16.67% of Python3 online submissions for Diagonal Traverse.

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return None
        go_up = True
        rows = len(matrix)
        columns = len(matrix[0])
        result = list()
        row = col = count = 0
        while count < rows * columns:
            if go_up:
                while row >= 0 and col < columns:
                    result.append(matrix[row][col])
                    row -= 1
                    col += 1
                    count += 1
                if row < 0 and col <= columns - 1:
                    row = 0
                if col == columns:
                    row += 2
                    col -= 1
            else:
                while col >= 0 and row < rows:
                    result.append(matrix[row][col])
                    row += 1
                    col -= 1
                    count += 1
                if col < 0 and row <= rows - 1:
                    col = 0
                if row == rows:
                    row -= 1
                    col += 2
            go_up = not go_up
        return result
