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
#Runtime: 60 ms
#Memory Usage: 14.1 MB

#Runtime: 60 ms, faster than 25.38% of Python3 online submissions for Valid Palindrome.
#Memory Usage: 14.1 MB, less than 48.81% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i].isalnum():
                if s[j].isalnum():
                    if s[i].lower() == s[j].lower():
                        i += 1
                        j -= 1
                    else:
                        return False
                else:
                    j -= 1
            else:
                i += 1
        return True
