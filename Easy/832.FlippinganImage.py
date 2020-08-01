"""
    Given a binary matrix A, we want to flip the image horizontally, then 
    invert it, and return the resulting image.
    To flip an image horizontally means that each row of the image is reversed.  
    For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
    To invert an image means that each 0 is replaced by 1, and each 1 is 
    replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

    Example:
    Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
    Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

    Notes:
        - 1 <= A.length = A[0].length <= 20
        - 0 <= A[i][j] <= 1
"""
#Difficulty: Easy
#82 / 82 test cases passed.
#Runtime: 48 ms
#Memory Usage: 13.6 MB

#Runtime: 48 ms, faster than 92.68% of Python3 online submissions for Flipping an Image.
#Memory Usage: 13.6 MB, less than 93.20% of Python3 online submissions for Flipping an Image.

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            i = 0
            j = len(row) - 1
            while i <= j:
                row[i], row[j] = abs(row[j] - 1), abs(row[i] - 1)
                i += 1
                j -= 1
        return A
