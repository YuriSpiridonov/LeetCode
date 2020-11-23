"""
    Given two string arrays word1 and word2, return true if the two arrays 
    represent the same string, and false otherwise.

    A string is represented by an array if the array elements concatenated 
    in order forms the string.

    Example:
    Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
    Output: true
    Explanation:
                 word1 represents string "ab" + "c" -> "abc"
                 word2 represents string "a" + "bc" -> "abc"
                 The strings are the same, so return true.

    Example:
    Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
    Output: false

    Example:
    Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
    Output: true

    Constraints:
        - 1 <= word1.length, word2.length <= 10^3
        - 1 <= word1[i].length, word2[i].length <= 10^3
        - 1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
        - word1[i] and word2[i] consist of lowercase letters.
"""
#Difficulty: Easy
#104 / 104 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14.3 MB

#Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Check If Two String Arrays are Equivalent.
#Memory Usage: 14.3 MB, less than 25.00% of Python3 online submissions for Check If Two String Arrays are Equivalent.

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
