"""
    Given a positive integer K, you need to find the length of the smallest 
    positive integer N such that N is divisible by K, and N only contains 
    the digit 1.

    Return the length of N. If there is no such N, return -1.

    Note: N may not fit in a 64-bit signed integer.

    Example:
    Input: K = 1
    Output: 1
    Explanation: The smallest answer is N = 1, which has length 1.

    Example:
    Input: K = 2
    Output: -1
    Explanation: There is no such positive integer N divisible by 2.

    Example:
    Input: K = 3
    Output: 3
    Explanation: The smallest answer is N = 111, which has length 3.

    Constraints:
        - 1 <= K <= 105
"""
#Difficulty: Medium
#70 / 70 test cases passed.
#Runtime: 2020 ms
#Memory Usage: 14.3 MB

#Runtime: 2020 ms, faster than 22.62% of Python3 online submissions for Smallest Integer Divisible by K.
#Memory Usage: 14.3 MB, less than 50.60% of Python3 online submissions for Smallest Integer Divisible by K.

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        n = 1
        count = 1
        if not K % 2 or not K % 5:
            return -1
        while n % K:
            n = n*10 + 1
            count += 1
        return count
