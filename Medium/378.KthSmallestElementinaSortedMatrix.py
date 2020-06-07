"""
    Given a n x n matrix where each of the rows and columns are sorted in 
    ascending order, find the kth smallest element in the matrix.
    Note that it is the kth smallest element in the sorted order, not the 
    kth distinct element.
    
    Example:
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ],
    k = 8,
    return 13.
    
    Note:
    You may assume k is always valid, 1 ≤ k ≤ n2.
"""
#Difficulty: Medium
#85 / 85 test cases passed.
#Runtime: 168 ms
#Memory Usage: 19.6 MB

#Runtime: 168 ms, faster than 96.92% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
#Memory Usage: 19.6 MB, less than 88.87% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        x= []
        for row in matrix:
            x += row
        x.sort()
        return x[k-1]
