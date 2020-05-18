"""
    Given an array of integers A sorted in non-decreasing order, return an 
    array of the squares of each number, also in sorted non-decreasing order.
    
    Example:
    Input: [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
"""
#Difficulty: Easy
#132 / 132 test cases passed.
#Runtime: 228 ms
#Memory Usage: 15.1 MB

#Runtime: 228 ms, faster than 78.60% of Python3 online submissions for Squares of a Sorted Array.
#Memory Usage: 15.1 MB, less than 44.05% of Python3 online submissions for Squares of a Sorted Array.

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i, n in enumerate(A):
            A[i] = n**2
        A.sort()
        return A
