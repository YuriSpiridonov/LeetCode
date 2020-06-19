"""
    Given a string s, the power of the string is the maximum length of a 
    non-empty substring that contains only one unique character.
    
    Return the power of the string.
    
    Example:
    Input: s = "leetcode"
    Output: 2
    Explanation: The substring "ee" is of length 2 with the character 'e' only.
    
    Constraints:
        - 1 <= s.length <= 500
        - s contains only lowercase English letters.
"""
#Difficulty: Easy
#333 / 333 test cases passed.
#Runtime: 36 ms
#Memory Usage: 13.7 MB

#Runtime: 36 ms, faster than 94.53% of Python3 online submissions for Consecutive Characters.
#Memory Usage: 13.7 MB, less than 88.51% of Python3 online submissions for Consecutive Characters.

class Solution:
    def maxPower(self, s: str) -> int:
        result = count = 1
        i = 0
        j = i + 1
        l = len(s) - 1
        while i < l:
            if j <= l and s[j] == s[i]:
                count += 1
                j += 1
            else:
                result = max(result, count)
                count = 1
                i = j
                j = i + 1
        return result
