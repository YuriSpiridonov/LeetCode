'''
    You are given an n x n 2D matrix representing an image, 
    rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you 
    have to modify the input 2D matrix directly. DO NOT 
    allocate another 2D matrix and do the rotation.

    Example:
        [[1,2,3],          [[7,4,1],
        [4,5,6],    ->     [8,5,2],
        [7,8,9]]           [9,6,3]]
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

    Example:
        [[ 5, 1, 9,11],          [[15,13, 2, 5],
        [ 2, 4, 8,10],    ->     [14, 3, 4, 1],
        [13, 3, 6, 7],           [12, 6, 8, 9],
        [15,14,12,16]]           [16, 7,10,11]]
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    Example:
    Input: matrix = [[1]]
    Output: [[1]]

    Example:
    Input: matrix = [[1,2],[3,4]]
    Output: [[3,1],[4,2]]

    Constraints:
        - matrix.length == n
        - matrix[i].length == n
        - 1 <= n <= 20
        - -1000 <= matrix[i][j] <= 1000
'''
#Difficulty: Medium
#21 / 21 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14.2 MB

#Runtime: 24 ms, faster than 99.06% of Python3 online submissions for Rotate Image.
#Memory Usage: 14.2 MB, less than 61.05% of Python3 online submissions for Rotate Image.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        while i < len(matrix)//2:
            j = len(matrix) - 1 - i
            l = 0
            while l < j-i:
                matrix[i+l][j], matrix[j][j-l], matrix[j-l][i], matrix[i][i+l] = matrix[i][i+l], matrix[i+l][j], matrix[j][j-l], matrix[j-l][i]
                l += 1
            i += 1