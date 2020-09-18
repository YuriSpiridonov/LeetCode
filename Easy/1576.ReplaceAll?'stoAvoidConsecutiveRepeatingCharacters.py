"""
    Given a string s containing only lower case English letters and the '?' 
    character, convert all the '?' characters into lower case letters such that 
    the final string does not contain any consecutive repeating characters. 
    You cannot modify the non '?' characters.

    It is guaranteed that there are no consecutive repeating characters in the 
    given string except for '?'.

    Return the final string after all the conversions (possibly zero) have been 
    made. If there is more than one solution, return any of them. It can be 
    shown that an answer is always possible with the given constraints.

    Example:
    Input: s = "?zs"
    Output: "azs"
    Explanation: There are 25 solutions for this problem. From "azs" to "yzs", 
                 all are valid. Only "z" is an invalid modification as the 
                 string will consist of consecutive repeating characters in 
                 "zzs".

    Example:
    Input: s = "ubv?w"
    Output: "ubvaw"
    Explanation: There are 24 solutions for this problem. Only "v" and "w" are 
                 invalid modifications as the strings will consist of 
                 consecutive repeating characters in "ubvvw" and "ubvww".

    Example:
    Input: s = "j?qg??b"
    Output: "jaqgacb"

    Example:
    Input: s = "??yw?ipkj?"
    Output: "acywaipkja"

    Constraints:
        - 1 <= s.length <= 100
        - s contains only lower case English letters and '?'.
"""
#Difficulty: Easy
#776 / 776 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.8 MB

#Runtime: 28 ms, faster than 86.44% of Python3 online submissions for Replace All ?'s to Avoid Consecutive Repeating Characters.
#Memory Usage: 13.8 MB, less than 56.12% of Python3 online submissions for Replace All ?'s to Avoid Consecutive Repeating Characters.

import random

class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        prev = nxt = None
        letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        for i, char in enumerate(s):
            if char == '?':
                if i-1 >= 0:
                    prev = ord(s[i-1]) - 97
                    letters.remove(prev)
                if i+1 < len(s) and s[i+1] != '?' and ord(s[i+1]) - 97 in letters:
                    nxt = ord(s[i+1]) - 97
                    letters.remove(nxt)
                letter = random.choice(letters) + 97
                letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
                s[i] = chr(letter)
        return ''.join(s)
