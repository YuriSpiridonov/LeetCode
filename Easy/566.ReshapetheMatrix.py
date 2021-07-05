'''
    In MATLAB, there is a handy function called reshape which 
    can reshape an m x n matrix into a new one with a different 
    size r x c keeping its original data.

    You are given an m x n matrix mat and two integers r and 
    c representing the row number and column number of the 
    wanted reshaped matrix.

    The reshaped matrix should be filled with all the elements 
    of the original matrix in the same row-traversing order 
    as they were.

    If the reshape operation with given parameters is possible 
    and legal, output the new reshaped matrix; Otherwise, 
    output the original matrix.

    Example:
    Input: mat = [[1,2],[3,4]], r = 1, c = 4
    Output: [[1,2,3,4]]

    Example:
    Input: mat = [[1,2],[3,4]], r = 2, c = 4
    Output: [[1,2],[3,4]]

    Constraints:
        - m == mat.length
        - n == mat[i].length
        - 1 <= m, n <= 100
        - -1000 <= mat[i][j] <= 1000
        - 1 <= r, c <= 300
'''
#Difficulty: Easy
#57 / 57 test cases passed.
#Runtime: 76 ms
#Memory Usage: 15 MB

#Runtime: 76 ms, faster than 99.31% of Python3 online submissions for Reshape the Matrix.
#Memory Usage: 15 MB, less than 41.26% of Python3 online submissions for Reshape the Matrix.

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        new_mat = [[] for _ in range(r)]
        k = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(new_mat[k]) == c:
                    k += 1
                new_mat[k].append(mat[i][j])
        return new_mat
