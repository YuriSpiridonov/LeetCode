"""
    Given an integer (signed 32 bits), write a function to check whether it is 
    a power of 4.

    Example:
    Input: 16
    Output: true

    Follow up: Could you solve it without loops/recursion?
"""
#Difficulty: Easy
#1060 / 1060 test cases passed.
#Runtime: 24 ms
#Memory Usage: 13.7 MB

#Runtime: 24 ms, faster than 96.97% of Python3 online submissions for Power of Four.
#Memory Usage: 13.7 MB, less than 78.95% of Python3 online submissions for Power of Four.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num in [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]:
            return True
        return False
