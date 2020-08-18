"""
    Return all non-negative integers of length N such that the absolute 
    difference between every two consecutive digits is K.
    Note that every number in the answer must not have leading zeros except for 
    the number 0 itself. For example, 01 has one leading zero and is invalid, 
    but 0 is valid.
    You may return the answer in any order.

    Example:
    Input: N = 3, K = 7
    Output: [181,292,707,818,929]
    Explanation: Note that 070 is not a valid number, because it has leading 
                 zeroes.

    Example:
    Input: N = 2, K = 1
    Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

    Note:
        1. 1 <= N <= 9
        2. 0 <= K <= 9
"""
#Difficulty: Medium
#92 / 92 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.2 MB

#Runtime: 28 ms, faster than 99.53% of Python3 online submissions for Numbers With Same Consecutive Differences.
#Memory Usage: 14.2 MB, less than 21.86% of Python3 online submissions for Numbers With Same Consecutive Differences.

class Solution:

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        self.K = K
        self.nums = []
        if N == 1:
            return [n for n in range(10)]
        for num in range(1, 10):
            self.dfs(N-1, num)
        return self.nums

    def dfs(self, N, num):
        if N == 0:
            self.nums.append(num)
            return
        digit = num % 10
        if digit >= self.K:
            self.dfs(N-1, num*10+digit-self.K)
        if self.K > 0 and digit + self.K < 10:
            self.dfs(N-1, num*10+digit+self.K)
