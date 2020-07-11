"""
    Given two strings s and t, determine if they are isomorphic.
    Two strings are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character 
    while preserving the order of characters. No two characters may map to the 
    same character but a character may map to itself.

    Example:
    Input: s = "paper", t = "title"
    Output: true

    Note:
        You may assume both s and t have the same length.
"""
#Difficulty: Easy
#32 / 32 test cases passed.
#Runtime: 48 ms
#Memory Usage: 14 MB

#Runtime: 48 ms, faster than 45.10% of Python3 online submissions for Isomorphic Strings.
#Memory Usage: 14 MB, less than 64.61% of Python3 online submissions for Isomorphic Strings.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            elif t[i] not in d.values():
                d[s[i]] = t[i]
            else:
                return False
        return True
