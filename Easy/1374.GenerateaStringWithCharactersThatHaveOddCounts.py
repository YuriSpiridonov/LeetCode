"""
    Given an integer n, return a string with n characters such that each 
    character in such string occurs an odd number of times.

    The returned string must contain only lowercase English letters. If there 
    are multiples valid strings, return any of them.  

    Example:
    Input: n = 4
    Output: "pppz"
    Explanation: "pppz" is a valid string since the character 'p' occurs three 
                 times and the character 'z' occurs once. Note that there are 
                 many other valid strings such as "ohhh" and "love".

    Example:
    Input: n = 2
    Output: "xy"
    Explanation: "xy" is a valid string since the characters 'x' and 'y' occur 
                 once. Note that there are many other valid strings such as 
                 "ag" and "ur".

    Example:
    Input: n = 7
    Output: "holasss"

    Constraints:
        - 1 <= n <= 500
"""
#Difficulty: Easy
#103 / 103 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.8 MB

#Runtime: 28 ms, faster than 81.87% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
#Memory Usage: 13.8 MB, less than 70.96% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.

class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' * n if n % 2 else 'b' + 'a' * (n - 1)
