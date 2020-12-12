'''
    For a string sequence, a string word is k-repeating if word 
    concatenated k times is a substring of sequence. The word's 
    maximum k-repeating value is the highest value k where word 
    is k-repeating in sequence. If word is not a substring of 
    sequence, word's maximum k-repeating value is 0.

    Given strings sequence and word, return the maximum 
    k-repeating value of word in sequence.

    Example:
    Input: sequence = "ababc", word = "ab"
    Output: 2
    Explanation: "abab" is a substring in "ababc".

    Example:
    Input: sequence = "ababc", word = "ba"
    Output: 1
    Explanation: "ba" is a substring in "ababc". "baba" is not 
                 a substring in "ababc".

    Example:
    Input: sequence = "ababc", word = "ac"
    Output: 0
    Explanation: "ac" is not a substring in "ababc". 

    Constraints:
        - 1 <= sequence.length <= 100
        - 1 <= word.length <= 100
        - sequence and word contains only lowercase English 
          letters.
'''
#Difficulty: Easy
#211 / 211 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14.2 MB

#Runtime: 24 ms, faster than 96.10% of Python3 online submissions for Maximum Repeating Substring.
#Memory Usage: 14.2 MB, less than 75.28% of Python3 online submissions for Maximum Repeating Substring.

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        x = 1
        while word*x in sequence:
            x += 1
        return x-1
