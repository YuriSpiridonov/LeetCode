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
#Runtime: 28 ms
#Memory Usage: 13.6 MB

#Runtime: 28 ms, faster than 88.81% of Python3 online submissions for Power of Four.
#Memory Usage: 13.6 MB, less than 93.86% of Python3 online submissions for Power of Four.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:  
        if num != 0:
            return (num & (num - 1) == 0) & len(bin(num)) % 2 == 1
        return False
