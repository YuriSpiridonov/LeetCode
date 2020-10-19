"""
    Given a string s, return the length of the longest substring between two 
    equal characters, excluding the two characters. If there is no such 
    substring return -1.
    A substring is a contiguous sequence of characters within a string.

    Example:
    Input: s = "aa"
    Output: 0
    Explanation: The optimal substring here is an empty substring between the 
                 two 'a's.

    Example:
    Input: s = "abca"
    Output: 2
    Explanation: The optimal substring here is "bc".

    Example:
    Input: s = "cbzxy"
    Output: -1
    Explanation: There are no characters that appear twice in s.

    Example:
    Input: s = "cabbac"
    Output: 4
    Explanation: The optimal substring here is "abba". Other non-optimal 
                 substrings include "bb" and "".

    Constraints:
        - 1 <= s.length <= 300
        - s contains only lowercase English letters.
"""
#Diffculty: Easy
#54 / 54 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14 MB

#Runtime: 32 ms, faster than 85.62% of Python3 online submissions for Largest Substring Between Two Equal Characters.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Largest Substring Between Two Equal Characters.

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        chars = set(s)
        reverse = s[::-1]
        length = 0
        if len(chars) == len(s):
            return -1
        for char in chars:
            i = 1 + s.index(char)
            j = 1 + reverse.index(char)
            length = max(length, len(s[i:-j]))
        return length
