'''
    Given a List of words, return the words that can be typed 
    using letters of alphabet on only one row's of American 
    keyboard like the image below.

    Example:
    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]

    Note:
        1. You may use one character in the keyboard more 
           than once.
        2. You may assume the input string will only contain 
           letters of alphabet.
'''
#Difficulty: Easy
#22 / 22 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.2 MB

#Runtime: 32 ms, faster than 43.03% of Python3 online submissions for Keyboard Row.
#Memory Usage: 14.2 MB, less than 21.89% of Python3 online submissions for Keyboard Row.

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        i = 0
        keyboard_rows = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1,
                         'u': 1, 'i': 1, 'o': 1, 'p': 1, 'a': 2, 's': 2, 
                         'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 
                         'l': 2, 'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 
                         'n': 3, 'm': 3}
        while i < len(words):
            row = None
            word = words[i]
            for char in set(word.lower()):
                if not row:
                    row = keyboard_rows[char]
                if keyboard_rows[char] != row:
                    words.pop(i)
                    i -= 1
                    break
            i += 1
        return words
