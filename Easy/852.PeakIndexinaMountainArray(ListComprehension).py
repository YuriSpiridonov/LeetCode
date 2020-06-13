"""
    Let's call an array A a mountain if the following properties hold:
    - A.length >= 3
    - There exists some 0 < i < A.length - 1 such that 
      A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    - Given an array that is definitely a mountain, return any i such that 
      A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
    
    Example:
    Input: [0,2,1,0]
    Output: 1
    
    Note:
        1. 3 <= A.length <= 10000
        2. 0 <= A[i] <= 10^6
        3. A is a mountain, as defined above.
"""
#Difficulty: Easy
#32 / 32 test cases passed.
#Runtime: 72 ms
#Memory Usage: 15.1 MB

#Runtime: 72 ms, faster than 94.64% of Python3 online submissions for Peak Index in a Mountain Array.
#Memory Usage: 15.1 MB, less than 49.72% of Python3 online submissions for Peak Index in a Mountain Array.

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return [i for i in range(1,len(A)) if A[i-1] < A[i] > A[i+1]][0]
