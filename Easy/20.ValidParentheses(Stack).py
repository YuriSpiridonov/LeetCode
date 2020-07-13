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
#Runtime: 28 ms
#Memory Usage: 13.8 MB        

#Runtime: 28 ms, faster than 82.23% of Python3 online submissions for Valid Parentheses.
#Memory Usage: 13.8 MB, less than 64.83% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(':')', '{':'}', '[':']'}
        stack = []
        for b in s: # take bracket 'b' from string 's'
            if b in parentheses: # if bracket in parentheses
                stack.append(parentheses[b]) # append it's opposite to stack
            elif not stack or stack.pop() != b: # if not stack or bracket not 
                return False                    # equal last bracket in stack
        return not stack # if stack still exists -> False else True
