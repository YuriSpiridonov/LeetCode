"""
    Given a string s and an integer k, return the length of the longest 
    substring of s such that the frequency of each character in this substring 
    is less than or equal to k.

    Example:
    Input: s = "aaabb", k = 3
    Output: 3
    Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

    Example:
    Input: s = "ababbc", k = 2
    Output: 5
    Explanation: The longest substring is "ababb", as 'a' is repeated 2 times 
                 and 'b' is repeated 3 times.

    Constraints:
        - 1 <= s.length <= 10^4
        - s consists of only lowercase English letters.
        - 1 <= k <= 10^5
"""
#Difficulty: Medium
#31 / 31 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14.5 MB

#Runtime: 24 ms, faster than 98.68% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
#Memory Usage: 14.5 MB, less than 16.41% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.

import collections

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        chars = collections.Counter(s)
        for char, count in chars.items():
            if count < k:
                length = 0
                subs = s.split(char)
                for sub in subs:
                    length = max(length, self.longestSubstring(sub, k))
                return length
        return len(s)
