'''
    Starting with a positive integer N, we reorder the 
    digits in any order (including the original order) such 
    that the leading digit is not zero.

    Return true if and only if we can do this in a way such 
    that the resulting number is a power of 2.

    Example:
    Input: 1
    Output: true

    Example:
    Input: 10
    Output: false

    Example:
    Input: 16
    Output: true

    Example:
    Input: 24
    Output: false

    Example:
    Input: 46
    Output: true

    Note:
        1. 1 <= N <= 10^9
'''
#Difficulty: Medium
#135 / 135 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.2 MB

#Runtime: 32 ms, faster than 81.85% of Python3 online submissions for Reordered Power of 2.
#Memory Usage: 14.2 MB, less than 52.82% of Python3 online submissions for Reordered Power of 2.

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        N = sorted(str(N))
        for x in range(30):
            if N == sorted(str(2**x)):
                return True
        return False