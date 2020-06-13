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
#Runtime: 76 ms
#Memory Usage: 15.4 MB

#Runtime: 76 ms, faster than 82.37% of Python3 online submissions for Peak Index in a Mountain Array.
#Memory Usage: 15.4 MB, less than 5.19% of Python3 online submissions for Peak Index in a Mountain Array.
    
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        s = sorted(set(A), reverse=True)
        for n in s:
            i = A.index(n)
            if A[i-1] < n > A[i+1]:
                return i
