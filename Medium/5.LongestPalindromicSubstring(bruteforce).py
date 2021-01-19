'''
    Given a string s, return the longest palindromic substring in s.

    Example:
    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Example:
    Input: s = "cbbd"
    Output: "bb"

    Example:
    Input: s = "a"
    Output: "a"

    Example:
    Input: s = "ac"
    Output: "a"

    Constraints:
        - 1 <= s.length <= 1000
        - s consist of only digits and English letters 
          (lower-case and/or upper-case),
'''
#Difficulty: Medium
#176 / 176 test cases passed.
#Runtime: 9028 ms
#Memory Usage: 14.3 MB

#Runtime: 9028 ms, faster than 5.03% of Python3 online submissions for Longest Palindromic Substring.
#Memory Usage: 14.3 MB, less than 63.00% of Python3 online submissions for Longest Palindromic Substring.

class Solution:

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        palindrome = ''
        palindrome_length = 0
        for i in range(length):
            j = i+1
            while j <= length:
                if self.isPalindrome(s[i:j]) and palindrome_length < len(s[i:j]):
                    palindrome = s[i:j]
                    palindrome_length = len(s[i:j])
                    if palindrome_length == length:
                        return palindrome
                j += 1
        return palindrome
    
    def isPalindrome(self, s):
        return s == s[::-1]