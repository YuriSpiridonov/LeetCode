"""
    Implement function ToLowerCase() that has a string parameter str, and 
    returns the same string in lowercase.

    Example:
    Input: "Hello"
    Output: "hello"
"""
#Difficulty: Easy
#8 / 8 test cases passed.
#Runtime: 20 ms
#Memory Usage: 14 MB

#Runtime: 20 ms, faster than 98.48% of Python3 online submissions for To Lower Case.
#Memory Usage: 14 MB, less than 15.97% of Python3 online submissions for To Lower Case.    

class Solution:
    def toLowerCase(self, s: str) -> str:
        length = len(s)
        for i in range(length):
            if ord(s[i]) in range(65, 91):
                s = s[:i] + chr(ord(s[i]) + 32) + s[i+1:]
        return s

#Runtime: 28 ms, faster than 72.96% of Python3 online submissions for To Lower Case.
#Memory Usage: 13.9 MB, less than 40.32% of Python3 online submissions for To Lower Case.
  
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ''
        for c in s:
            if ord(c) in range(65, 91):
                ans += chr(ord(c) + 32)
            else:
                ans += c
        return ans
