'''
    An array is monotonic if it is either monotone increasing 
    or monotone decreasing.

    An array A is monotone increasing if for all i <= j, 
    A[i] <= A[j].  An array A is monotone decreasing if for 
    all i <= j, A[i] >= A[j].

    Return true if and only if the given array A is monotonic.

    Example:
    Input: [1,2,2,3]
    Output: true

    Example:
    Input: [6,5,4,4]
    Output: true

    Example:
    Input: [1,3,2]
    Output: false

    Example:
    Input: [1,2,4,5]
    Output: true

    Example:
    Input: [1,1,1]
    Output: true

    Note:
        1. 1 <= A.length <= 50000
        2. -100000 <= A[i] <= 100000
'''
#Difficulty: Easy
#366 / 366 test cases passed.
#Runtime: 440 ms
#Memory Usage: 20.6 MB

#Runtime: 440 ms, faster than 93.04% of Python3 online submissions for Monotonic Array.
#Memory Usage: 20.6 MB, less than 14.35% of Python3 online submissions for Monotonic Array.

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return sorted(A) in [A, A[::-1]]
