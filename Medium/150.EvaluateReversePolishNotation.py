"""
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    Valid operators are +, -, *, /. Each operand may be an integer or another 
    expression.

    Note:
        - Division between two integers should truncate toward zero.
        - The given RPN expression is always valid. That means the expression 
          would always evaluate to a result and there won't be any divide by 
          zero operation.

    Example:
    Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    Output: 22
    Explanation: 
      ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
"""
#Difficulty: Medium
#20 / 20 test cases passed.
#Runtime: 68 ms
#Memory Usage: 14 MB

#Runtime: 68 ms, faster than 84.65% of Python3 online submissions for Evaluate Reverse Polish Notation.
#Memory Usage: 14 MB, less than 84.34% of Python3 online submissions for Evaluate Reverse Polish Notation.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                if token == '+': stack.append(x + y)
                if token == '-': stack.append(x - y)
                if token == '*': stack.append(x * y)
                if token == '/': stack.append(int(x / y))
        return stack[0]
