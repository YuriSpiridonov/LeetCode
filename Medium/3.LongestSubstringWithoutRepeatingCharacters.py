"""
    Given a string s, find the length of the longest substring without 
    repeating characters.

    Example:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                 Notice that the answer must be a substring, "pwke" is a 
                 subsequence and not a substring.

    Example:
    Input: s = ""
    Output: 0

    Constraints:
        - 0 <= s.length <= 5 * 104
        - s consists of English letters, digits, symbols and spaces.
"""
#Difficulty: Medium
#987 / 987 test cases passed.
#Runtime: 172 ms
#Memory Usage: 14.2 MB

#Runtime: 172 ms, faster than 20.74% of Python3 online submissions for Longest Substring Without Repeating Characters.
#Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        lss = 0
        length = len(s)
        if length < 2:
            return length
        s += s[-1]
        while j <= length:
            if len(set(s[i:j])) < len(s[i:j]):
                i += 1
            lss = max(lss, len(s[i:j]))
            j += 1
        return lss
