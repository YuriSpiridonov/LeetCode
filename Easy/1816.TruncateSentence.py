'''
    A sentence is a list of words that are separated by a 
    single space with no leading or trailing spaces. Each 
    of the words consists of only uppercase and lowercase 
    English letters (no punctuation).
        - For example, "Hello World", "HELLO", and "hello 
          world hello world" are all sentences.

    You are given a sentence s​​​​​​ and an integer k​​​​​​. You want 
    to truncate s​​​​​​ such that it contains only the first k​​​​​​ 
    words. Return s​​​​​​ after truncating it.

    Example:
    Input: s = "Hello how are you Contestant", k = 4
    Output: "Hello how are you"
    Explanation: The words in s are ["Hello", "how" "are", 
                 "you", "Contestant"].
                 The first 4 words are ["Hello", "how", "are", "you"].
                 Hence, you should return "Hello how are you".

    Example:
    Input: s = "What is the solution to this problem", k = 4
    Output: "What is the solution"
    Explanation: The words in s are ["What", "is" "the", 
                 "solution", "to", "this", "problem"].
                 The first 4 words are ["What", "is", "the", 
                 "solution"].
                 Hence, you should return "What is the solution".

    Example:
    Input: s = "chopper is not a tanuki", k = 5
    Output: "chopper is not a tanuki"

    Constraints:
        - 1 <= s.length <= 500
        - k is in the range [1, the number of words in s].
        - s consist of only lowercase and uppercase English 
          letters and spaces.
        - The words in s are separated by a single space.
        - There are no leading or trailing spaces.
'''
#Dfficulty: Easy
#72 / 72 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.3 MB

#Runtime: 32 ms, faster than 69.33% of Python3 online submissions for Truncate Sentence.
#Memory Usage: 14.3 MB, less than 55.62% of Python3 online submissions for Truncate Sentence.

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        for i in range(len(s)):
            if s[i] == ' ':
                k -= 1
            if not k:
                return s[:i]
        return s