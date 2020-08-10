"""
    Given a column title as appear in an Excel sheet, return its corresponding 
    column number.

    For example:

            A -> 1
            B -> 2
            C -> 3
            ...
            Z -> 26
            AA -> 27
            AB -> 28 
            ...

    Example:
    Input: "AB"
    Output: 28

    Example:
    Input: "ZY"
    Output: 701

    Constraints:
        - 1 <= s.length <= 7
        - s consists only of uppercase English letters.
        - s is between "A" and "FXSHRXW".
"""
#Difficulty: Easy
#1000 / 1000 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.7 MB

#Runtime: 28 ms, faster than 92.13% of Python3 online submissions for Excel Sheet Column Number.
#Memory Usage: 13.7 MB, less than 83.68% of Python3 online submissions for Excel Sheet Column Number.

class Solution:
    def titleToNumber(self, s: str) -> int:
        number, prod = 0, 1
        for char in s[::-1]:
            number += (1 + ord(char) - ord('A')) * prod
            prod *= 26
        return number
