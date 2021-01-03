'''
    Suppose you have n integers from 1 to n. We define a 
    beautiful arrangement as an array that is constructed by 
    these n numbers successfully if one of the following is 
    true for the ith position (1 <= i <= n) in this array:
        - The number at the ith position is divisible by i.
        - i is divisible by the number at the ith position.

    Given an integer n, return the number of the beautiful 
    arrangements that you can construct.

    Example:
    Input: n = 2
    Output: 2
    Explanation: 
                 - The first beautiful arrangement is [1, 2]:
                 - Number at the 1st position (i=1) is 1, and 
                   1 is divisible by i (i=1).
                 - Number at the 2nd position (i=2) is 2, and 
                   2 is divisible by i (i=2).
                 - The second beautiful arrangement is [2, 1]:
                 - Number at the 1st position (i=1) is 2, and 
                   2 is divisible by i (i=1).
                 - Number at the 2nd position (i=2) is 1, and 
                   i (i=2) is divisible by 1.

    Example:
    Input: n = 1
    Output: 1

    Constraints:
        - 1 <= n <= 15
'''
#Difficulty: Medium
#15 / 15 test cases passed.
#Runtime: 2608 ms
#Memory Usage: 14.2 MB

#Runtime: 2608 ms, faster than 5.48% of Python3 online submissions for Beautiful Arrangement.
#Memory Usage: 14.2 MB, less than 74.19% of Python3 online submissions for Beautiful Arrangement.

class Solution:

    def countArrangement(self, n: int) -> int:
        self.result = 0
        self.dfs(n)
        return self.result

    def dfs(self, n, array=[], i=1):
        if i-1 == n:
            self.result += 1
            return
        for m in range(n):
            m += 1
            if m not in array and (not m%i or not i%m):
                array.append(m)
                i += 1
                self.dfs(n, array, i)
                array.remove(m)
                i -= 1
