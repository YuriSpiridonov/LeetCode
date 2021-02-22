'''
    Given a string and a string dictionary, find the longest 
    string in the dictionary that can be formed by deleting 
    some characters of the given string. If there are more 
    than one possible results, return the longest word with 
    the smallest lexicographical order. If there is no 
    possible result, return the empty string.

    Example:
    Input:
    s = "abpcplea", d = ["ale","apple","monkey","plea"]
    Output: 
    "apple"

    Example:
    Input:
    s = "abpcplea", d = ["a","b","c"]
    Output: 
    "a"

    Note:
        1. All the strings in the input will only contain 
           lower-case letters.
        2. The size of the dictionary won't exceed 1,000.
        3. The length of all the strings in the input won't 
           exceed 1,000.
'''
#Difficulty: Medium
#31 / 31 test cases passed.
#Runtime: 76 ms
#Memory Usage: 16.9 MB

#Runtime: 76 ms, faster than 95.90% of Python3 online submissions for Longest Word in Dictionary through Deleting.
#Memory Usage: 16.9 MB, less than 38.92% of Python3 online submissions for Longest Word in Dictionary through Deleting.

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longest_word = ''
        for word in d:
            chars = s
            flag = True
            for char in word:
                if char in chars:
                    chars = chars[1+chars.index(char):]
                else:
                    flag = False
                    break
            if flag and (len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word)):
                longest_word = word
        return longest_word