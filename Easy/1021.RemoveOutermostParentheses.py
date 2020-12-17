'''
    A valid parentheses string is either empty (""), 
    "(" + A + ")", or A + B, where A and B are valid 
    parentheses strings, and + represents string concatenation.  
    For example, "", "()", "(())()", and "(()(()))" are all 
    valid parentheses strings.

    A valid parentheses string S is primitive if it is nonempty, 
    and there does not exist a way to split it into S = A+B, 
    with A and B nonempty valid parentheses strings.

    Given a valid parentheses string S, consider its primitive 
    decomposition: S = P_1 + P_2 + ... + P_k, where P_i are 
    primitive valid parentheses strings.

    Return S after removing the outermost parentheses of every 
    primitive string in the primitive decomposition of S.

    Example:
    Input: "(()())(())"
    Output: "()()()"
    Explanation: The input string is "(()())(())", with p
                 rimitive decomposition "(()())" + "(())".
                 After removing outer parentheses of each 
                 part, this is "()()" + "()" = "()()()".

    Example:
    Input: "(()())(())(()(()))"
    Output: "()()()()(())"
    Explanation: The input string is "(()())(())(()(()))", 
                 with primitive decomposition 
                            "(()())" + "(())" + "(()(()))".
                 After removing outer parentheses of each 
                 part, this is "()()" + "()" + "()(())" = 
                 "()()()()(())".

    Example:
    Input: "()()"
    Output: ""
    Explanation: The input string is "()()", with primitive 
                 decomposition "()" + "()".
                 After removing outer parentheses of each 
                 part, this is "" + "" = "".

    Note:
        1. S.length <= 10000
        2. S[i] is "(" or ")"
        3. S is a valid parentheses string
'''
#Difficulty: Easy
#59 / 59 test cases passed.
#Runtime: 60 ms
#Memory Usage: 14.6 MB

#Runtime: 60 ms, faster than 6.25% of Python3 online submissions for Remove Outermost Parentheses.
#Memory Usage: 14.6 MB, less than 5.29% of Python3 online submissions for Remove Outermost Parentheses.

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        l, r, i, j = 0, 0, 0, None
        S = list(S)
        while i < len(S):
            if S[i] == '(':
                l += 1
            else:
                r += 1
            if j is None:
                j = i
            if l == r:
                S.pop(i)
                S.pop(j)
                l, r, j = 0, 0, None
                i -= 2
            i += 1
        return ''.join(S)
