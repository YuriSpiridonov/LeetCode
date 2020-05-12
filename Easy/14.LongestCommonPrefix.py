"""
    Write a function to find the longest common prefix string amongst an array 
    of strings.
    If there is no common prefix, return an empty string "".
    
    Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"
"""
#Difficulty: Easy
#118 / 118 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14 MB

#Runtime: 24 ms, faster than 97.59% of Python3 online submissions for Longest Common Prefix.
#Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        if len(strs) == 1: return strs[0]
        i = 0
        strs = sorted(strs, key=len)
        word = strs[0]
        for letter in word:
            if self.counter(strs[1:], letter, i):
                i += 1
            else: break
        return word[:i]

    def counter(self, strs, letter, i):
        for word in strs:
            if letter not in word[i]:
                return 0
        return 1
