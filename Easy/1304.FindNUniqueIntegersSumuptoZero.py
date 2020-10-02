"""
    Given an integer n, return any array containing n unique integers such that 
    they add up to 0.

    Example:
    Input: n = 5
    Output: [-7,-1,1,3,4]
    Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

    Example:
    Input: n = 3
    Output: [-1,0,1]

    Example:
    Input: n = 1
    Output: [0]

    Constraints:
        - 1 <= n <= 1000
"""
#Difficulty: Easy
#42 / 42 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.3 MB

#Runtime: 32 ms, faster than 72.59% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
#Memory Usage: 14.3 MB, less than 5.20% of Python3 online submissions for Find N Unique Integers Sum up to Zero.

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2:
            result.append(0)
            n -= 1
        while n:
            result.extend([n, -n])
            n -= 2
        return result
