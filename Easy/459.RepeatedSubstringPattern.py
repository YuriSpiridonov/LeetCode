"""
    Given a non-empty string check if it can be constructed by taking a 
    substring of it and appending multiple copies of the substring together. 
    You may assume the given string consists of lowercase English letters only 
    and its length will not exceed 10000.

    Example:
    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.

    Example:
    Input: "aba"
    Output: False

    Example:
    Input: "abcabcabcabc"
    Output: True
    Explanation: It's the substring "abc" four times. 
                 (And the substring "abcabc" twice.)
"""
#Difficulty: Easy
#120 / 120 test cases passed.
#Runtime: 124 ms
#Memory Usage: 13.6 MB

#Runtime: 124 ms, faster than 45.73% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 13.6 MB, less than 96.45% of Python3 online submissions for Repeated Substring Pattern.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        l = 1 + length // 2
        i = 1
        while i < l:
            if s[:i] * (length // i) == s:
                return True
            i += 1
        return False
