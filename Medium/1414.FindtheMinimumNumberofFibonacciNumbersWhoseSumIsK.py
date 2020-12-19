'''
    Given an integer k, return the minimum number of Fibonacci 
    numbers whose sum is equal to k. The same Fibonacci number 
    can be used multiple times.

    The Fibonacci numbers are defined as:
        - F1 = 1
        - F2 = 1
        - Fn = Fn-1 + Fn-2 for n > 2.

    It is guaranteed that for the given constraints we can 
    always find such Fibonacci numbers that sum up to k.

    Example:
    Input: k = 7
    Output: 2 
    Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 
                 8, 13, ... 
                 For k = 7 we can use 2 + 5 = 7.

    Example:
    Input: k = 10
    Output: 2 
    Explanation: For k = 10 we can use 2 + 8 = 10.

    Example:
    Input: k = 19
    Output: 3 
    Explanation: For k = 19 we can use 1 + 5 + 13 = 19.

    Constraints:
        - 1 <= k <= 10^9
'''
#Difficulty: Medium
#503 / 503 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14 MB

#Runtime: 32 ms, faster than 83.81% of Python3 online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
#Memory Usage: 14 MB, less than 85.51% of Python3 online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        count = 0
        while fib[-1] < k:
            fib.append(fib[-2] + fib[-1])
        while k:
            f = fib.pop()
            if f <= k:
                k -= f
                count += 1
        return count
