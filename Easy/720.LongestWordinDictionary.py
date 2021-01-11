'''
    Given a list of strings words representing an English 
    Dictionary, find the longest word in words that can be 
    built one character at a time by other words in words. 
    If there is more than one possible answer, return the 
    longest word with the smallest lexicographical order.
    If there is no answer, return the empty string.

    Example:
    Input: 
    words = ["w","wo","wor","worl", "world"]
    Output: "world"
    Explanation: The word "world" can be built one character 
                 at a time by "w", "wo", "wor", and "worl".

    Example:
    Input: 
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    Output: "apple"
    Explanation: Both "apply" and "apple" can be built from 
                 other words in the dictionary. However, 
                 "apple" is lexicographically smaller than 
                 "apply".

    Note:
        - All the strings in the input will only contain 
          lowercase letters.
        - The length of words will be in the range [1, 1000].
        - The length of words[i] will be in the range [1, 30].
'''
#Difficulty: Easy
#57 / 57 test cases passed.
#Runtime: 288 ms
#Memory Usage: 15.6 MB

#Runtime: 288 ms, faster than 13.36% of Python3 online submissions for Longest Word in Dictionary.
#Memory Usage: 15.6 MB, less than 8.39% of Python3 online submissions for Longest Word in Dictionary.

class Solution:
    
    def __init__(self):
        self.chars = [None] * 26
        self.is_word = False

    def buildDict(self, words: List[str]) -> None:
        for word in words:
            current = self
            for char in word:
                i = ord(char)-ord('a')
                if not current.chars[i]:
                    current.chars[i] = Solution()
                current = current.chars[i]
            current.is_word = True

    def checkWord(self, word: str) -> str:
        current = self
        for char in word:
            i = ord(char)-ord('a')
            if current.chars[i] and current.chars[i].is_word:
                current = current.chars[i]
            else:
                return ''
        return word

    def longestWord(self, words: List[str]) -> str:
        result = ''
        self.buildDict(words)
        for word in words:
            longest = self.checkWord(word)
            if len(longest) > len(result):
                result = longest
            elif len(longest) == len(result):
                result = min(result, longest)
        return result
