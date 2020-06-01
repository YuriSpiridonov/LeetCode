"""
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
    Fibonacci sequence, such that each number is the sum of the two preceding 
    ones, starting from 0 and 1. That is,
    
        F(0) = 0,   F(1) = 1
        F(N) = F(N - 1) + F(N - 2), for N > 1.
    
    Given N, calculate F(N).
    
    Example:
    Input: 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

    Note:
    0 ≤ N ≤ 30.
"""
#Difficulty: Easy
#31 / 31 test cases passed.
#Runtime: 24 ms
#Memory Usage: 13.6 MB
        
#Runtime: 24 ms, faster than 93.52% of Python3 online submissions for Fibonacci Number.
#Memory Usage: 13.6 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.
    
class Solution:
    def fib(self, N: int) -> int:
        n1, n2 = 0, 1
        for i in range(N):
            n1, n2 = n2, n1 + n2
        return n1
