"""
    Given an integer n and an integer start.
    Define an array nums where nums[i] = start + 2*i (0-indexed) and 
                                                            n == nums.length.
    Return the bitwise XOR of all elements of nums.

    Example:
    Input: n = 5, start = 0
    Output: 8
    Explanation: Array nums is equal to [0, 2, 4, 6, 8] 
                 where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
    Where "^" corresponds to bitwise XOR operator.

    Constraints:
        - 1 <= n <= 1000
        - 0 <= start <= 1000
        - n == nums.length
"""
#Difficulty: Easy
#54 / 54 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.9 MB

#Runtime: 28 ms, faster than 85.34% of Python3 online submissions for XOR Operation in an Array.
#Memory Usage: 13.9 MB, less than 27.03% of Python3 online submissions for XOR Operation in an Array.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        num = start
        for i in range(1, n):
            num ^= start + 2 * i
        return num
