"""
    Given a sentence that consists of some words separated by a single space, 
    and a searchWord.
    You have to check if searchWord is a prefix of any word in sentence.
    Return the index of the word in sentence where searchWord is a prefix of 
    this word (1-indexed).
    If searchWord is a prefix of more than one word, return the index of the 
    first word (minimum index). If there is no such word return -1.
    A prefix of a string S is any leading contiguous substring of S.

    Example:
    Input: sentence = "i love eating burger", searchWord = "burg"
    Output: 4
    Explanation: "burg" is prefix of "burger" which is the 4th word in the 
                 sentence.
    
    Constraints:
        - 1 <= sentence.length <= 100
        - 1 <= searchWord.length <= 10
        - sentence consists of lowercase English letters and spaces.
        - searchWord consists of lowercase English letters.
"""
#Difficulty: Easy
#38 / 38 test cases passed.
#Runtime: 24 ms
#Memory Usage: 13.8 MB

#Runtime: 24 ms, faster than 94.74% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
#Memory Usage: 13.8 MB, less than 68.90% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentenc    
   
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        for index, word in enumerate(words):
            if searchWord in word and searchWord[0] == word[0]:
                return 1 + index
        return -1
