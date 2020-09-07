"""
    Given a pattern and a string str, find if str follows the same pattern.

    Here follow means a full match, such that there is a bijection between a 
    letter in pattern and a non-empty word in str.

    Example:
    Input: pattern = "abba", str = "dog cat cat dog"
    Output: true

    Example:
    Input:pattern = "abba", str = "dog cat cat fish"
    Output: false

    Example:
    Input: pattern = "aaaa", str = "dog cat cat dog"
    Output: false

    Example:
    Input: pattern = "abba", str = "dog dog dog dog"
    Output: false

    Notes:
        - You may assume pattern contains only lowercase letters, and str 
          contains lowercase letters that may be separated by a single space.
"""
#Difficulty: Easy
#37 / 37 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.7 MB

#Runtime: 28 ms, faster than 82.00% of Python3 online submissions for Word Pattern.
#Memory Usage: 13.7 MB, less than 84.35% of Python3 online submissions for Word Pattern.

class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        pairs = {}
        pattern = list(pattern)
        string = string.split(' ')
        if len(pattern) != len(string):
            return False
        for i, p in enumerate(pattern):
            if p not in pairs and string[i] not in pairs.values():
                pairs[p] = string[i]
            else:
                if p not in pairs or pairs[p] != string[i]:
                    return False
        return True
