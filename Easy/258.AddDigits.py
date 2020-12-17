'''
    Given a non-negative integer num, repeatedly add all its 
    digits until the result has only one digit.

    Example:
    Input: 38
    Output: 2 
    Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
                Since 2 has only one digit, return it.

    Follow up:
    Could you do it without any loop/recursion in O(1) 
    runtime?
'''
#Difficulty: Easy
#1101 / 1101 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14.2 MB

#Runtime: 36 ms, faster than 28.26% of Python3 online submissions for Add Digits.
#Memory Usage: 14.2 MB, less than 51.11% of Python3 online submissions for Add Digits.

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = num//10 + num%10
        return num
