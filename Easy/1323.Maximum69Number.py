"""
    Given a positive integer num consisting only of digits 6 and 9.
    Return the maximum number you can get by changing at most one digit 
    (6 becomes 9, and 9 becomes 6).

    Example:
    Input: num = 9669
    Output: 9969
    Explanation: 
                Changing the first digit results in 6669.
                Changing the second digit results in 9969.
                Changing the third digit results in 9699.
                Changing the fourth digit results in 9666. 
                The maximum number is 9969.

    Constraints:
        - 1 <= num <= 10^4
        - num's digits are 6 or 9.
"""
#Difficulty: Easy
#153 / 153 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.8 MB
    
#Runtime: 28 ms, faster than 82.26% of Python3 online submissions for Maximum 69 Number.
#Memory Usage: 13.6 MB, less than 96.45% of Python3 online submissions for Maximum 69 Number.    
    
class Solution:
    def maximum69Number (self, num: int) -> int:
        n = list(str(num))
        for i in range(len(n)):
            if n[i] < '9':
                n[i] = '9'
                break
        return int(''.join(n))
