'''
    Given two integers dividend and divisor, divide two 
    integers without using multiplication, division, and 
    mod operator.

    Return the quotient after dividing dividend by divisor.

    The integer division should truncate toward zero, which 
    means losing its fractional part. For example, 
    truncate(8.345) = 8 and truncate(-2.7335) = -2.

    Note:
        - Assume we are dealing with an environment that 
          could only store integers within the 32-bit signed 
          integer range: [−2^31,  2^31 − 1]. For this problem, 
          assume that your function returns 2^31 − 1 when the 
          division result overflows.

    Example:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = truncate(3.33333..) = 3.

    Example:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = truncate(-2.33333..) = -2.

    Example:
    Input: dividend = 0, divisor = 1
    Output: 0

    Example:
    Input: dividend = 1, divisor = 1
    Output: 1

    Constraints:
        - -2^31 <= dividend, divisor <= 2^31 - 1
        - divisor != 0
'''
#Difficulty: Medium
#989 / 989 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.3 MB

#Runtime: 28 ms, faster than 92.03% of Python3 online submissions for Divide Two Integers.
#Memory Usage: 14.3 MB, less than 58.58% of Python3 online submissions for Divide Two Integers.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min_number = -2**31
        max_number = 2**31 - 1
        result = abs(dividend) // abs(divisor)
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return min(result, max_number)
        else:
             return max(-result, min_number)