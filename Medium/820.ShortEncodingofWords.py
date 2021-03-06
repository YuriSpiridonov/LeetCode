'''
    A valid encoding of an array of words is any reference 
    string s and array of indices indices such that:

        - words.length == indices.length
        - The reference string s ends with the '#' character.
        - For each index indices[i], the substring of s 
          starting from indices[i] and up to (but not 
          including) the next '#' character is equal to 
          words[i].

    Given an array of words, return the length of the shortest 
    reference string s possible of any valid encoding of words.

    Example:
    Input: words = ["time", "me", "bell"]
    Output: 10
    Explanation: A valid encoding would be s = "time#bell#" 
                 and indices = [0, 2, 5].
                 - words[0] = "time", the substring of s 
                   starting from indices[0] = 0 to the next 
                   '#' is underlined in "time#bell#"
                 - words[1] = "me", the substring of s 
                   starting from indices[1] = 2 to the next 
                   '#' is underlined in "time#bell#"
                 - words[2] = "bell", the substring of s s
                   tarting from indices[2] = 5 to the next 
                   '#' is underlined in "time#bell#"

    Example:
    Input: words = ["t"]
    Output: 2
    Explanation: A valid encoding would be s = "t#" and 
                 indices = [0].

    Constraints:
        - 1 <= words.length <= 2000
        - 1 <= words[i].length <= 7
        - words[i] consists of only lowercase letters.
'''
#Difficulty: Medium
#33 / 33 test cases passed.
#Runtime: 276 ms
#Memory Usage: 15 MB

#Runtime: 276 ms, faster than 19.19% of Python3 online submissions for Short Encoding of Words.
#Memory Usage: 15 MB, less than 90.12% of Python3 online submissions for Short Encoding of Words.

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        string = ''
        words.sort(key=len, reverse=True)
        for word in words:
            if word + '#' not in string:
                string += word + '#'
        return len(string)
