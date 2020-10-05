"""
    Every non-negative integer N has a binary representation.  For example, 5 
    can be represented as "101" in binary, 11 as "1011" in binary, and so on.
    Note that except for N = 0, there are no leading zeroes in any binary 
    representation.

    The complement of a binary representation is the number in binary you get 
    when changing every 1 to a 0 and 0 to a 1.  For example, the complement of 
    "101" in binary is "010" in binary.

    For a given number N in base-10, return the complement of it's binary 
    representation as a base-10 integer.

    Example:
    Input: 5
    Output: 2
    Explanation: 5 is "101" in binary, with complement "010" in binary, which 
                 is 2 in base-10.

    Example:
    Input: 7
    Output: 0
    Explanation: 7 is "111" in binary, with complement "000" in binary, which 
                 is 0 in base-10.

    Example:
    Input: 10
    Output: 5
    Explanation: 10 is "1010" in binary, with complement "0101" in binary, 
                 which is 5 in base-10.

    Note:
        1. 0 <= N < 10^9
        2. This question is the same as 476: 
                               https://leetcode.com/problems/number-complement/
"""
#Difficulty: Easy
#128 / 128 test cases passed.
#Runtime: 20 ms
#Memory Usage: 14 MB

#Runtime: 20 ms, faster than 98.13% of Python3 online submissions for Complement of Base 10 Integer.
#Memory Usage: 14 MB, less than 16.64% of Python3 online submissions for Complement of Base 10 Integer.

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int(''.join(['0' if n =='1' else '1' for n in list(bin(N)[2:])]), 2)
