"""
    Two images A and B are given, represented as binary, square matrices of the 
    same size.  (A binary matrix has only 0s and 1s as values.)
    We translate one image however we choose (sliding it left, right, up, or 
    down any number of units), and place it on top of the other image.  After, 
    the overlap of this translation is the number of positions that have a 1 in 
    both images.
    (Note also that a translation does not include any kind of rotation.)
    What is the largest possible overlap?

    Example:
    Input: A = [[1,1,0],
                [0,1,0],
                [0,1,0]]
           B = [[0,0,0],
                [0,1,1],
                [0,0,1]]
    Output: 3
    Explanation: We slide A to right by 1 unit and down by 1 unit.

    Notes: 
        - 1 <= A.length = A[0].length = B.length = B[0].length <= 30
        - 0 <= A[i][j], B[i][j] <= 1
"""
#Difficulty: Medium
#49 / 49 test cases passed.
#Runtime: 2624 ms
#Memory Usage: 13.8 MB

#Runtime: 2624 ms, faster than 5.19% of Python3 online submissions for Image Overlap.
#Memory Usage: 13.8 MB, less than 90.91% of Python3 online submissions for Image Overlap.

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        size = len(A) - 1
        largest_overlap = 0
        for i in range(2 * size + 1):
            for j in range(2 * size + 1):
                i = size - i if i > size else i
                j = size - j if j > size else j
                overlap = 0
                for x in range(size + 1):
                    for y in range(size + 1):
                        if 0 <= x + i <= size and 0 <= y + j <= size and A[x][y] and A[x][y] == B[x+i][y+j]:
                            overlap += 1
                largest_overlap = max(largest_overlap, overlap)
        return largest_overlap
