"""
    Given two equal-size strings s and t. In one step you can choose any 
    character of t and replace it with another character.
    Return the minimum number of steps to make t an anagram of s.
    An Anagram of a string is a string that contains the same characters with 
    a different (or the same) ordering.
    
    Example:
    Input: s = "leetcode", t = "practice"
    Output: 5
    Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper 
                 characters to make t anagram of s.
    
    Constraints:
        - 1 <= s.length <= 50000
        - s.length == t.length
        - s and t contain lower-case English letters only.
"""
#Difficulty: Medium
#63 / 63 test cases passed.
#Runtime: 292 ms
#Memory Usage: 14.7 MB

#Runtime: 292 ms, faster than 32.39% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
#Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        intersection_letters = ''.join(list(set(s) & set(t)))
        intersection_value = 0
        if s != t:
            for letter in intersection_letters:
                intersection_value += min(s.count(letter), t.count(letter))
        return len(s) - intersection_value if s != t else 0
