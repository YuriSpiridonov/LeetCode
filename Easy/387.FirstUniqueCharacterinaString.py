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
#Runtime: 104 ms
#Memory Usage: 13.9 MB

#Runtime: 104 ms, faster than 71.09% of Python3 online submissions for First Unique Character in a String.
#Memory Usage: 13.9 MB, less than 46.48% of Python3 online submissions for First Unique Character in a String.    

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        mi = len(s)
        for index, letter in enumerate(s):
            if letter in d:
                if d[letter][0]:
                    d[letter][0] -= 1
                else:
                    continue
            else:
                d[letter] = [1, index]
        for value in d.values():
            if value[0] == 1:
                mi = min(mi, value[1])
        return mi if mi != len(s) else -1
