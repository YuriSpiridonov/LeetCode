"""
    Given a positive integer num, output its complement number. The complement 
    strategy is to flip the bits of its binary representation.

    Example:
    Input: num = 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), 
                 and its complement is 010. So you need to output 2.

    Example:
    Input: num = 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits), 
                 and its complement is 0. So you need to output 0.

    Constraints:
        - The given integer num is guaranteed to fit within the range of a 
          32-bit signed integer.
        - num >= 1
        - You could assume no leading zero bit in the integer’s binary 
          representation.
        - This question is the same as 1009: 
                   https://leetcode.com/problems/complement-of-base-10-integer/
"""
#Difficulty: Easy
#149 / 149 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.1 MB

#Runtime: 28 ms, faster than 77.02% of Python3 online submissions for Number Complement.
#Memory Usage: 14.1 MB, less than 6.63% of Python3 online submissions for Number Complement.

class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join(['0' if n =='1' else '1' for n in list(bin(num)[2:])]), 2)
