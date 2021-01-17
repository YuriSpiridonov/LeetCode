'''
    Given an integer n, return the number of strings of 
    length n that consist only of vowels (a, e, i, o, u) 
    and are lexicographically sorted.

    A string s is lexicographically sorted if for all valid 
    i, s[i] is the same as or comes before s[i+1] in the 
    alphabet.

    Example:
    Input: n = 1
    Output: 5
    Explanation: The 5 sorted strings that consist of vowels 
                 only are ["a","e","i","o","u"].

    Example:
    Input: n = 2
    Output: 15
    Explanation: The 15 sorted strings that consist of vowels 
                 only are ["aa","ae","ai","ao","au","ee",
                           "ei","eo","eu","ii","io","iu",
                           "oo","ou","uu"].
                 Note that "ea" is not a valid string since 
                 'e' comes after 'a' in the alphabet.

    Example:
    Input: n = 33
    Output: 66045

    Constraints:
        - 1 <= n <= 50 
'''
#Difficulty: Medium
#41 / 41 test cases passed.
#Runtime: 1288 ms
#Memory Usage: 161.4 MB

#Runtime: 1288 ms, faster than 18.87% of Python3 online submissions for Count Sorted Vowel Strings.
#Memory Usage: 161.4 MB, less than 5.48% of Python3 online submissions for Count Sorted Vowel Strings.

from itertools import combinations_with_replacement

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return len(list(combinations_with_replacement('aeiou', n)))