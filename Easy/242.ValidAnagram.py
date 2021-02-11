'''
    Given two strings s and t , write a function to determine 
    if t is an anagram of s.

    Example:
    Input: s = "anagram", t = "nagaram"
    Output: true

    Example:
    Input: s = "rat", t = "car"
    Output: false

    Note:
    You may assume the string contains only lowercase alphabets.

    Follow up:
    What if the inputs contain unicode characters? How would 
    you adapt your solution to such case?
'''
#Dfficulty: Easy
#34 / 34 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.5 MB

#Runtime: 32 ms, faster than 98.22% of Python3 online submissions for Valid Anagram.
#Memory Usage: 14.5 MB, less than 48.96% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t: return True
        if not s or not t or len(s) != len(t): return False
        i = 0
        c = set(s+t)
        result = False
        for l in c:
            if l in s and l in t and s.count(l) == t.count(l):
                result = True
                continue
            else:
                result = False
                break
        return result