"""
    Balanced strings are those who have equal quantity of 'L' and 'R' characters.
    Given a balanced string s split it in the maximum amount of balanced strings.
    Return the maximum amount of splitted balanced strings.

    Example:
    Input: s = "RLRRLLRLRL"
    Output: 4
    Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring 
                 contains same number of 'L' and 'R'.

    Example:
    Input: s = "RLLLLRRRLR"
    Output: 3
    Explanation: s can be split into "RL", "LLLRRR", "LR", each substring 
                 contains same number of 'L' and 'R'.

    Constraints:
        - 1 <= s.length <= 1000
        - s[i] = 'L' or 'R'
"""
#Diffculty: Easy
#40 / 40 test cases passed.
#Runtime: 36 ms
#Memory Usage: 13.9 MB

#Runtime: 36 ms, faster than 42.16% of Python3 online submissions for Split a String in Balanced Strings.
#Memory Usage: 13.9 MB, less than 37.65% of Python3 online submissions for Split a String in Balanced Strings.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        stack = []
        d = {'R' : 'L', 'L' : 'R'}
        for c in s:
            if c not in stack: 
                stack.append(d[c])
                continue
            stack.pop()
            if not stack:
                count += 1
        return count
