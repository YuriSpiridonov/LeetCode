'''
    Two strings are considered close if you can attain one 
    from the other using the following operations:

        - Operation 1: Swap any two existing characters.
            = For example, abcde -> aecdb
        - Operation 2: Transform every occurrence of one 
          existing character into another existing character, 
          and do the same with the other character.
            = For example, aacabb -> bbcbaa (all a's turn 
              into b's, and all b's turn into a's)

    You can use the operations on either string as many times 
    as necessary.

    Given two strings, word1 and word2, return true if word1 
    and word2 are close, and false otherwise.

    Example:
    Input: word1 = "abc", word2 = "bca"
    Output: true
    Explanation: You can attain word2 from word1 in 2 
                 operations.
                 Apply Operation 1: "abc" -> "acb"
                 Apply Operation 1: "acb" -> "bca"

    Example:
    Input: word1 = "a", word2 = "aa"
    Output: false
    Explanation: It is impossible to attain word2 from word1, 
                 or vice versa, in any number of operations.

    Example:
    Input: word1 = "cabbba", word2 = "abbccc"
    Output: true
    Explanation: You can attain word2 from word1 in 3 
                 operations.
                 Apply Operation 1: "cabbba" -> "caabbb"
                 Apply Operation 2: "caabbb" -> "baaccc"
                 Apply Operation 2: "baaccc" -> "abbccc"

    Example:
    Input: word1 = "cabbba", word2 = "aabbss"
    Output: false
    Explanation: It is impossible to attain word2 from word1, 
                 or vice versa, in any amount of operations.

    Constraints:
        - 1 <= word1.length, word2.length <= 10^5
        - word1 and word2 contain only lowercase English 
          letters.
'''
#Difficulty: Medium
#144 / 144 test cases passed.
#Runtime: 160 ms
#Memory Usage: 15.3 MB

#Runtime: 160 ms, faster than 50.82% of Python3 online submissions for Determine if Two Strings Are Close.
#Memory Usage: 15.3 MB, less than 76.23% of Python3 online submissions for Determine if Two Strings Are Close.

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        chars1 = set(word1)
        chars2 = set(word2)
        letters1 = Counter(word1)
        letters2 = Counter(word2)
        return chars1 == chars2 and sorted(letters1.values()) == sorted(letters2.values())