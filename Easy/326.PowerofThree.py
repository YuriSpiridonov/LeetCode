'''
    Given an integer n, return true if it is a power of 
    three. Otherwise, return false.

    An integer n is a power of three, if there exists an 
    integer x such that n == 3x.

    Example:
    Input: n = 27
    Output: true

    Example:
    Input: n = 0
    Output: false

    Example:
    Input: n = 9
    Output: true

    Example:
    Input: n = 45
    Output: false

    Constraints:
        - -2^31 <= n <= 2^31 - 1
    
    Follow up: Could you solve it without loops/recursion?
'''
#Difficulty: Easy
#21038 / 21038 test cases passed.
#Runtime: 188 ms
#Memory Usage: 14.3 MB

#Runtime: 188 ms, faster than 6.05% of Python3 online submissions for Power of Three.
#Memory Usage: 14.3 MB, less than 47.05% of Python3 online submissions for Power of Three.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 0
        while 3 ** x <= n:
            if 3 ** x == n:
                return True
            x += 1
        return False