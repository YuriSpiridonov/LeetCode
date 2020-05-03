"""
  Given a 32-bit signed integer, reverse digits of an integer.

  Example 1:
  Input: 123
  Output: 321
  
  Example 2:
  Input: -123
  Output: -321
"""
#Difficulty: Easy
#1032 / 1032 test cases passed.
#Runtime: 24 ms
#Memory Usage: 13.9 MB

#Runtime: 24 ms, faster than 95.17% of Python3 online submissions for Reverse Integer.
#Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:
        if -2147483648 <= x <= 2147483647:
            if x < 0:
                x = abs(x)
                x = 0-Solution.reverser(x)
            else:
                x = Solution.reverser(x)
        return x if -2147483648 <= x <= 2147483647 else 0

    def reverser(x):
        nn = 0
        while x:
            lastDigit = x % 10
            nn = nn * 10 + lastDigit
            x = x // 10
        return nn
