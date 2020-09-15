"""
    Given a string s consists of upper/lower-case alphabets and empty space 
    characters ' ', return the length of last word (last word means the last 
    appearing word if we loop from left to right) in the string.
    If the last word does not exist, return 0.
    Note: A word is defined as a maximal substring consisting of non-space 
    characters only.

    Example:
    Input: "Hello World"
    Output: 5
"""
#Difficulty: Easy
#59 / 59 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14 MB

#Runtime: 24 ms, faster than 91.10% of Python3 online submissions for Length of Last Word.
#Memory Usage: 14 MB, less than 37.01% of Python3 online submissions for Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.rstrip().split(" ")
        return len(words[-1])
