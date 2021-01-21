'''
    Given a non-negative integer num represented as a string, 
    remove k digits from the number so that the new number 
    is the smallest possible.

    Note:
        - The length of num is less than 10002 and will 
          be ≥ k.
        - The given num does not contain any leading zero.

    Example:
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to 
                 form the new number 1219 which is the 
                 smallest.

    Example:
    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. 
                 Note that the output must not contain 
                 leading zeroes.

    Example:
    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and 
                 it is left with nothing which is 0.
'''
#Difficlty: Medium
#33 / 33 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.1 MB

#Runtime: 32 ms, faster than 92.66% of Python3 online submissions for Remove K Digits.
#Memory Usage: 14.1 MB, less than 99.94% of Python3 online submissions for Remove K Digits.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        length = len(num) - k
        stack = []
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        while stack and stack[0] == '0':
            stack.pop(0)
        return ''.join(stack)[:length] if stack and length else '0'