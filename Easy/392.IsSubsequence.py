"""
    Given a string s and a string t, check if s is subsequence of t.

    A subsequence of a string is a new string which is formed from the original 
    string by deleting some (can be none) of the characters without disturbing 
    the relative positions of the remaining characters. 
    (ie, "ace" is a subsequence of "abcde" while "aec" is not).

    Follow up:
    If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and 
    you want to check one by one to see if T has its subsequence. In this 
    scenario, how would you change your code?

    Credits:
    Special thanks to @pbrother for adding this problem and creating all test 
    cases.

    Example:
    Input: s = "abc", t = "ahbgdc"
    Output: true

    Example:
    Input: s = "axc", t = "ahbgdc"
    Output: false

    Constraints:
        - 0 <= s.length <= 100
        - 0 <= t.length <= 10^4
        - Both strings consists only of lowercase characters.
"""
#Difficulty: Easy
#15 / 15 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.2 MB

#Runtime: 28 ms, faster than 84.55% of Python3 online submissions for Is Subsequence.
#Memory Usage: 14.2 MB, less than 32.25% of Python3 online submissions for Is Subsequence.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            if char in t:
                i = t.index(char)
                t = t[i+1:]
            else:
                return False
        return True
