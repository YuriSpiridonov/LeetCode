"""
    Given two positive integers n and k.

    A factor of an integer n is defined as an integer i where n % i == 0.

    Consider a list of all factors of n sorted in ascending order, 
    return the kth factor in this list or return -1 if n has less 
    than k factors.

    Example:
    Input: n = 12, k = 3
    Output: 3
    Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

    Example:
    Input: n = 7, k = 2
    Output: 7
    Explanation: Factors list is [1, 7], the 2nd factor is 7.

    Example:
    Input: n = 4, k = 4
    Output: -1
    Explanation: Factors list is [1, 2, 4], there is only 3 factors. 
                 We should return -1.

    Example:
    Input: n = 1, k = 1
    Output: 1
    Explanation: Factors list is [1], the 1st factor is 1.

    Example:
    Input: n = 1000, k = 3
    Output: 4
    Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 
                 125, 200, 250, 500, 1000].

    Constraints:
        - 1 <= k <= n <= 1000
"""
#Difficulty: Medium
#207 / 207 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.1 MB

#Runtime: 28 ms, faster than 87.17% of Python3 online submissions for The kth Factor of n.
#Memory Usage: 14.1 MB, less than 76.75% of Python3 online submissions for The kth Factor of n.

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        while i <= n:
            if not n % i:
                k -= 1
                if k == 0:
                    return i
            i += 1
        return -1
