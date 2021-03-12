'''
    Given a binary string s and an integer k.

    Return True if every binary code of length k is a 
    substring of s. Otherwise, return False.

    Example:
    Input: s = "00110110", k = 2
    Output: true
    Explanation: The binary codes of length 2 are "00", "01", 
                 "10" and "11". They can be all found as 
                 substrings at indicies 0, 1, 3 and 2 
                 respectively.

    Example:
    Input: s = "00110", k = 2
    Output: true

    Example:
    Input: s = "0110", k = 1
    Output: true
    Explanation: The binary codes of length 1 are "0" and "1", 
                 it is clear that both exist as a substring. 

    Example:
    Input: s = "0110", k = 2
    Output: false
    Explanation: The binary code "00" is of length 2 and 
                 doesn't exist in the array.

    Example:
    Input: s = "0000000001011100", k = 4
    Output: false

    Constraints:
        - 1 <= s.length <= 5 * 10^5
        - s consists of 0's and 1's only.
        - 1 <= k <= 20
'''
#Difficuty: Medium
#196 / 196 test cases passed.
#Runtime: 6064 ms
#Memory Usage: 18.3 MB

#Runtime: 6064 ms, faster than 9.71% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
#Memory Usage: 18.3 MB, less than 96.20% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.

from itertools import product

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substrings = product(['0', '1'], repeat=k)
        for substring in substrings:
            string = ''.join(substring)
            if string not in s:
                return False
        return True