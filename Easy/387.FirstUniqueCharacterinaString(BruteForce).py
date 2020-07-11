"""
    Given a string, find the first non-repeating character in it and return its 
    index. If it doesn't exist, return -1.

    Examples:
    s = "leetcode"
    return 0.
    s = "loveleetcode"
    return 2.

    Note: You may assume the string contains only lowercase English letters.
"""
#Difficulty: Easy
#104 / 104 test cases passed.
#Runtime: 9232 ms
#Memory Usage: 13.9 MB

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        for index, letter in enumerate(s):
            if s.count(letter) == 1:
                return index
        return -1
