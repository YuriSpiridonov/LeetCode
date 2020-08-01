"""
    Given a word, you need to judge whether the usage of capitals in it is right 
    or not.
    We define the usage of capitals in a word to be right when one of the 
    following cases holds:
        1. All letters in this word are capitals, like "USA".
        2. All letters in this word are not capitals, like "leetcode".
        3. Only the first letter in this word is capital, like "Google".
    Otherwise, we define that this word doesn't use capitals in a right way.

    Example:
    Input: "USA"
    Output: True

    Example:
    Input: "FlaG"
    Output: False

    Note: The input will be a non-empty word consisting of uppercase and 
          lowercase latin letters.
"""
#Difficulty: Easy
#550 / 550 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.8 MB

#Runtime: 28 ms, faster than 86.51% of Python3 online submissions for Detect Capital.
#Memory Usage: 13.8 MB, less than 57.14% of Python3 online submissions for Detect Capital.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
