"""
    Implement a basic calculator to evaluate a simple expression string.

    The expression string contains only non-negative integers, +, -, *, / 
    operators and empty spaces . The integer division should truncate toward 
    zero.

    Example:
    Input: "3+2*2"
    Output: 7

    Example:
    Input: " 3/2 "
    Output: 1

    Example:
    Input: " 3+5 / 2 "
    Output: 5

    Note:
        - You may assume that the given expression is always valid.
        - Do not use the eval built-in library function.
"""
#Difficulty: Medium
#109 / 109 test cases passed.
#Runtime: 4176 ms
#Memory Usage: 17.4 MB

#Runtime: 4176 ms, faster than 5.05% of Python3 online submissions for Basic Calculator II.
#Memory Usage: 17.4 MB, less than 14.94% of Python3 online submissions for Basic Calculator II.

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        result = 0
        num = 0
        prev = 0
        operator = '+'
        queue = []
        for char in s:
            queue.append(char)
        while queue:
            n = queue.pop(0)
            if n.isdigit():
                num = num * 10 + int(n)
            if n in '+-*/' or not queue:
                if operator == '+':
                    result += prev
                    prev = num
                elif operator == '-':
                    result += prev
                    prev = -num
                elif operator == '*':
                    prev *= num
                else:
                    prev = int(prev/num)
                if not queue:
                    result += prev
                else:
                    operator = n
                num = 0
        return result
