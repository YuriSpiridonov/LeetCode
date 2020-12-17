'''
    A decimal number is called deci-binary if each of its 
    digits is either 0 or 1 without any leading zeros. 
    For example, 101 and 1100 are deci-binary, while 112 
    and 3001 are not.

    Given a string n that represents a positive decimal 
    integer, return the minimum number of positive deci-binary 
    numbers needed so that they sum up to n.

    Example:
    Input: n = "32"
    Output: 3
    Explanation: 10 + 11 + 11 = 32

    Example:
    Input: n = "82734"
    Output: 8

    Example:
    Input: n = "27346209830709182346"
    Output: 9

    Constraints:
        - 1 <= n.length <= 10^5
        - n consists of only digits.
        - n does not contain any leading zeros and represents 
          a positive integer.
'''
#Difficulty: Medium
#94 / 94 test cases passed.
#Runtime: 64 ms
#Memory Usage: 14.7 MB

#Runtime: 64 ms, faster than 50.00% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
#Memory Usage: 14.7 MB, less than 25.00% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)
