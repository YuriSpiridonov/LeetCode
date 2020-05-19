"""
    Given a string, determine if it is a palindrome, considering only 
    alphanumeric characters and ignoring cases.
    Note: For the purpose of this problem, we define empty string as valid 
    palindrome.
    
    Example:
    Input: "A man, a plan, a canal: Panama"
    Output: true
"""
#Difficulty: Easy
#476 / 476 test cases passed.
#Runtime: 44 ms
#Memory Usage: 15.4 MB

#Runtime: 44 ms, faster than 78.91% of Python3 online submissions for Valid Palindrome.
#Memory Usage: 15.4 MB, less than 9.52% of Python3 online submissions for Valid Palindrome.

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W', '', s).lower()
        return s == s[::-1]
