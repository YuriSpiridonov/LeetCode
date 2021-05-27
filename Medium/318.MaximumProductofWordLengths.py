'''
    Given a string array words, return the maximum value of 
    length(word[i]) * length(word[j]) where the two words do 
    not share common letters. If no such two words exist, 
    return 0.

    Example:
    Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    Output: 16
    Explanation: The two words can be "abcw", "xtfn".

    Example:
    Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
    Output: 4
    Explanation: The two words can be "ab", "cd".

    Example:
    Input: words = ["a","aa","aaa","aaaa"]
    Output: 0
    Explanation: No such pair of words.

    Constraints:
        - 2 <= words.length <= 1000
        - 1 <= words[i].length <= 1000
        - words[i] consists only of lowercase English 
          letters.
'''
#Difficulty: Medium
#167 / 167 test cases passed.
#Runtime: 6204 ms
#Memory Usage: 14.7 MB

#Runtime: 6204 ms, faster than 6.57% of Python3 online submissions for Maximum Product of Word Lengths.
#Memory Usage: 14.7 MB, less than 67.98% of Python3 online submissions for Maximum Product of Word Lengths.

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = sorted(set(words), key=len, reverse=True)
        length = len(words)
        result = 0
        for i in range(length):
            row = max([len(words[i]) * len(word) if not (set(words[i]) & set(word)) else 0 for word in words])
            result = max(result, row)
        return result