'''
    You are given two strings s1 and s2 of equal length. A 
    string swap is an operation where you choose two indices 
    in a string (not necessarily different) and swap the 
    characters at these indices.

    Return true if it is possible to make both strings equal 
    by performing at most one string swap on exactly one of 
    the strings. Otherwise, return false.

    Example:
    Input: s1 = "bank", s2 = "kanb"
    Output: true
    Explanation: For example, swap the first character with 
                 the last character of s2 to make "bank".

    Example:
    Input: s1 = "attack", s2 = "defend"
    Output: false
    Explanation: It is impossible to make them equal with 
                 one string swap.

    Example:
    Input: s1 = "kelb", s2 = "kelb"
    Output: true
    Explanation: The two strings are already equal, so no 
                 string swap operation is required.

    Example:
    Input: s1 = "abcd", s2 = "dcba"
    Output: false

    Constraints:
        - 1 <= s1.length, s2.length <= 100
        - s1.length == s2.length
        - s1 and s2 consist of only lowercase English 
          letters.
'''
#Difficulty: Easy
#129 / 129 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.3 MB

#Runtime: 28 ms, faster than 81.95% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.
#Memory Usage: 14.3 MB, less than 52.92% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count in [0, 2] and set(s1) == set(s2)