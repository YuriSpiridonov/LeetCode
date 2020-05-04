"""
    Determine whether an integer is a palindrome. An integer is a palindrome 
    when it reads the same backward as forward.
    
    Example:
    Input: 121
    Output: true
    
    Example:
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, 
    it becomes 121-. Therefore it is not a palindrome.
    
    Follow up:
    Coud you solve it without converting the integer to a string? # Done
"""
#Difficulty: Easy
#11509 / 11509 test cases passed.
#Runtime: 56 ms
#Memory Usage: 13.9 MB

#Runtime: 56 ms, faster than 79.26 % of Python3 online submissions for Palindrome Number.
#Memory Usage: 13.9 MB, less than 6.50% of Python3 online submissions for Palindrome Number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        return self.reverse(x) == x
    
    def reverse(self, x):
        y = 0
        while x:
            d = x % 10
            y = y * 10 + d
            x //= 10
        return y
