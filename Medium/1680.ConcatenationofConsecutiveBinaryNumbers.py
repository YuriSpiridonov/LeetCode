'''
    Given an integer n, return the decimal value of the binary 
    string formed by concatenating the binary representations 
    of 1 to n in order, modulo 109 + 7.

    Example:
    Input: n = 1
    Output: 1
    Explanation: "1" in binary corresponds to the decimal 
                 value 1. 

    Example:
    Input: n = 3
    Output: 27
    Explanation: In binary, 1, 2, and 3 corresponds to "1", 
                 "10", and "11".
                 After concatenating them, we have "11011", 
                 which corresponds to the decimal value 27.

    Example:
    Input: n = 12
    Output: 505379714
    Explanation: The concatenation results in 
                 "1101110010111011110001001101010111100".
                 The decimal value of that is 118505380540.
                 After modulo 109 + 7, the result is 505379714.

    Constraints:
        - 1 <= n <= 10^5
'''
#Difficulty:Medium
#403 / 403 test cases passed.
#Runtime: 1540 ms
#Memory Usage: 16.2 MB

#Runtime: 1540 ms, faster than 65.90% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
#Memory Usage: 16.2 MB, less than 38.68% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        x = 1
        y = 1000000000
        binary = ''
        while x <= n:
            binary += bin(x)[2:]
            x += 1
        num = int(binary, 2)
        return num if num < y else num % (y+7)
