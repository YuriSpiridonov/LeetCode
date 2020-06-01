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
#Runtime: 12 ms
#Memory Usage: 13.8 MB

#Runtime: 12 ms, faster than 99.99% of Python3 online submissions for Fibonacci Number.
#Memory Usage: 13.8 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.

class Solution:
    def fib(self, N: int) -> int:
        fib = [0,1,1]
        if N <= 2:
            return fib[N]
        while True:
            i = len(fib) - 1
            fib.append(fib[i] + fib[i-1])
            if i == N - 1: # if i == N:
                break
        return sum(fib[-3:-1]) # return fib[N]
