"""
    Given a non-empty string s and a dictionary wordDict containing a list of 
    non-empty words, determine if s can be segmented into a space-separated 
    sequence of one or more dictionary words.

    Note:
        - The same word in the dictionary may be reused multiple times in the 
          segmentation.
        - You may assume the dictionary does not contain duplicate words.

    Example:
    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

    Example:
    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as 
                 "apple pen apple".
                 Note that you are allowed to reuse a dictionary word.

    Example:
    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: false
"""
#Difficulty: Medium
#43 / 43 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14.3 MB

#Runtime: 40 ms, faster than 71.18% of Python3 online submissions for Word Break.
#Memory Usage: 14.3 MB, less than 7.70% of Python3 online submissions for Word Break.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s += ' '
        length = len(s) - 1
        words = [True] + [False] * length
        for i in range(length+1):
            j = 0
            while j < i:
                if words[j] and s[j:i] in wordDict:
                    words[i] = True
                    break
                j += 1
        return words[length]
