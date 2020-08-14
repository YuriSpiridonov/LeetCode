"""
    Given a string which consists of lowercase or uppercase letters, find the 
    length of the longest palindromes that can be built with those letters.
    This is case sensitive, for example "Aa" is not considered a palindrome 
    here.

    Note:
    Assume the length of given string will not exceed 1,010.

    Example:
    Input:
            "abccccdd"
    Output:
            7
    Explanation:
                One longest palindrome that can be built is "dccaccd", 
                whose length is 7.
"""
#Difficulty: Easy
#95 / 95 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14 MB

#Runtime: 28 ms, faster than 91.20% of Python3 online submissions for Longest Palindrome.
#Memory Usage: 14 MB, less than 9.61% of Python3 online submissions for Longest Palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars_set = set(s)
        length = 0
        odd = 0
        for char in chars_set:
            count = s.count(char)
            if count % 2:
                odd += 1
            length += count
        return length - odd + 1 if odd else length
