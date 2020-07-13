"""
    Given a string containing just the characters '(', ')', '{', '}', '[', ']', 
    determine if the input string is valid.

    An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.

    Note that an empty string is also considered valid.

    Example:
    Input: "()[]{}"
    Output: true
"""
#Difficulty: Easy
#76 / 76 test cases passed.
#Runtime: 44 ms
#Memory Usage: 14 MB

#Runtime: 44 ms, faster than 23.31% of Python3 online submissions for Valid Parentheses.
#Memory Usage: 14 MB, less than 25.86% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'()', '{}', '[]'}
        length = len(s)
        if length < 2:
            return not s
        i = 1
        while s:
            if s[i-1:i+1] in parentheses:
                s = s[:i-1] + s[i+1:]
                i -= 1
            else:
                i += 1
            if i == length:
                break
        return not s
