"""
    Write a function that takes a string as input and reverse only the vowels 
    of a string.

    Example:
    Input: "hello"
    Output: "holle"

    Example:
    Input: "leetcode"
    Output: "leotcede"

    Note:
        - The vowels does not include the letter "y".
"""
#Difficulty: Easy
#481 / 481 test cases passed.
#Runtime: 184 ms
#Memory Usage: 14.4 MB

#Runtime: 184 ms, faster than 7.25% of Python3 online submissions for Reverse Vowels of a String.
#Memory Usage: 14.4 MB, less than 96.24% of Python3 online submissions for Reverse Vowels of a String.

class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        l = len(s) - 1
        #vowels = 'aAeEiIoOuU'
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while i < l:
            if s[i] in vowels:
                while s[l] not in vowels:
                    l -= 1
                if i < l:
                    s = s[:i] + s[l] + s[i+1:l] + s[i] + s[l+1:]
                    i += 1
                    l -= 1
                    continue
            i += 1
        return s
