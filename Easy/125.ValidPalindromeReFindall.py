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
#Runtime: 40 ms
#Memory Usage: 15 MB

#Runtime: 40 ms, faster than 88.62% of Python3 online submissions for Valid Palindrome.
#Memory Usage: 15 MB, less than 9.52% of Python3 online submissions for Valid Palindrome.
        
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall(r'\w+', s)).lower()
        length = len(s)
        mid = length//2
        left = s[:mid]
        return left[::-1] == s[mid+1:] if length % 2 != 0 else left[::-1] == s[mid:]
