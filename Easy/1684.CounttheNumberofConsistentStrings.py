'''
    You are given a string allowed consisting of distinct 
    characters and an array of strings words. A string is 
    consistent if all characters in the string appear in the 
    string allowed.

    Return the number of consistent strings in the array words.

    Example:
    Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
    Output: 2
    Explanation: Strings "aaab" and "baa" are consistent since 
                 they only contain characters 'a' and 'b'.

    Example:
    Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
    Output: 7
    Explanation: All strings are consistent.

    Example:
    Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
    Output: 4
    Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

    Constraints:
        - 1 <= words.length <= 10^4
        - 1 <= allowed.length <= 26
        - 1 <= words[i].length <= 10
        - The characters in allowed are distinct.
        - words[i] and allowed contain only lowercase 
          English letters.
'''
#Difficulty: Easy
#74 / 74 test cases passed.
#Runtime: 248 ms
#Memory Usage: 16.3 MB

#Runtime: 248 ms, faster than 75.00% of Python3 online submissions for Count the Number of Consistent Strings.
#Memory Usage: 16.3 MB, less than 25.00% of Python3 online submissions for Count the Number of Consistent Strings.

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        for word in words:
            word = set(word)
            for char in word:
                if char not in allowed:
                    count -= 1
                    break
        return count
