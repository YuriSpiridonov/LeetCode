"""
    Given an integer n, return the number of trailing zeroes in n!.

    Follow up: Could you write a solution that works in logarithmic time 
    complexity?

    Example:
    Input: n = 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.

    Example:
    Input: n = 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.

    Example:
    Input: n = 0
    Output: 0

    Constraints:
        - 1 <= n <= 10^4
"""
#Difficulty: Easy
#500 / 500 test cases passed.
#Runtime: 4236 ms
#Memory Usage: 14.3 MB

#Runtime: 4236 ms, faster than 11.06% of Python3 online submissions for Factorial Trailing Zeroes.
#Memory Usage: 14.3 MB, less than 16.42% of Python3 online submissions for Factorial Trailing Zeroes.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        f = 1
        while n > 0:
            f = f * n
            n -= 1
        f = str(f)[::-1]
        count = float(inf)
        for i in range(1,10):
            i = str(i)
            if i in f:
                count = min(count, f.index(i))
        return count
