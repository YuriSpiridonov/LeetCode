'''
    In an alien language, surprisingly they also use english 
    lowercase letters, but possibly in a different order. 
    The order of the alphabet is some permutation of 
    lowercase letters.

    Given a sequence of words written in the alien language, 
    and the order of the alphabet, return true if and only 
    if the given words are sorted lexicographicaly in this 
    alien language.

    Example:
    Input: words = ["hello","leetcode"], 
           order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, 
                 then the sequence is sorted.

    Example:
    Input: words = ["word","world","row"], 
           order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, 
                 then words[0] > words[1], hence the sequence 
                 is unsorted.

    Example:
    Input: words = ["apple","app"], 
           order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, 
                 and the second string is shorter (in size.) 
                 According to lexicographical rules 
                 "apple" > "app", because 'l' > '∅', where 
                 '∅' is defined as the blank character which 
                 is less than any other character (More info).

    Constraints:
        - 1 <= words.length <= 100
        - 1 <= words[i].length <= 20
        - order.length == 26
        - All characters in words[i] and order are English 
          lowercase letters.
'''
#Difficuty: Easy
#119 / 119 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14.1 MB

#Runtime: 36 ms, faster than 61.59% of Python3 online submissions for Verifying an Alien Dictionary.
#Memory Usage: 14.1 MB, less than 98.44% of Python3 online submissions for Verifying an Alien Dictionary.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        prev = words[0]

        for i, c in enumerate(order):
            alphabet[c] = i

        for word in words[1:]:
            length = min(len(prev), len(word))
            for i in range(length):
                if alphabet[prev[i]] == alphabet[word[i]]:
                    if i == length-1 and length != len(prev):
                        return False
                    continue
                elif alphabet[prev[i]] < alphabet[word[i]]:
                    prev = word
                    break
                else:
                    return False
        return True