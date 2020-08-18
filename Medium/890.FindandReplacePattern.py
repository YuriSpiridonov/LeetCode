"""
    You have a list of words and a pattern, and you want to know which words in 
    words matches the pattern.
    A word matches the pattern if there exists a permutation of letters p so 
    that after replacing every letter x in the pattern with p(x), we get the 
    desired word.
    (Recall that a permutation of letters is a bijection from letters to 
    letters: every letter maps to another letter, and no two letters map to the 
    same letter.)
    Return a list of the words in words that match the given pattern. 
    You may return the answer in any order.

    Example:
    Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    Output: ["mee","aqq"]
    Explanation: "mee" matches the pattern because there is a permutation 
                                                         {a -> m, b -> e, ...}. 
                 "ccc" does not match the pattern because {a -> c, b -> c, ...} 
                 is not a permutation, since a and b map to the same letter.

    Note:
        - 1 <= words.length <= 50
        - 1 <= pattern.length = words[i].length <= 20
"""
#Difficulty: Medium
#46 / 46 test cases passed.
#Runtime: 36 ms
#Memory Usage: 13.8 MB

#Runtime: 36 ms, faster than 62.82% of Python3 online submissions for Find and Replace Pattern.
#Memory Usage: 13.8 MB, less than 70.46% of Python3 online submissions for Find and Replace Pattern.

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        l = len(pattern)
        patterns = []
        for word in words:
            match = True
            d = {}
            for i in range(l):
                if pattern[i] not in d:
                    if not d.values() or d.values() and word[i] not in d.values():
                        d[pattern[i]] = word[i]
                    else:
                        match = False
                        break
                else:
                    if d[pattern[i]] != word[i]:
                        match = False
                        break
            if match:
                patterns.append(word)
        return patterns
