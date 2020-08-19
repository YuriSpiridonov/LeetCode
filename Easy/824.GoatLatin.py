"""
    A sentence S is given, composed of words separated by spaces. Each word 
    consists of lowercase and uppercase letters only.
    We would like to convert the sentence to "Goat Latin" 
    (a made-up language similar to Pig Latin.)

    The rules of Goat Latin are as follows:
        - If a word begins with a vowel (a, e, i, o, or u), append "ma" to the 
          end of the word.
          For example, the word 'apple' becomes 'applema'.
        - If a word begins with a consonant (i.e. not a vowel), remove the 
          first letter and append it to the end, then add "ma".
          For example, the word "goat" becomes "oatgma".
        - Add one letter 'a' to the end of each word per its word index in the 
          sentence, starting with 1.
          For example, the first word gets "a" added to the end, the second 
          word gets "aa" added to the end and so on.
          Return the final sentence representing the conversion from S to Goat 
          Latin. 

    Example:
    Input: "I speak Goat Latin"
    Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

    Example:
    Input: "The quick brown fox jumped over the lazy dog"
    Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa 
                                    hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

    Notes:
        - S contains only uppercase, lowercase and spaces. Exactly one space 
          between each word.
        - 1 <= S.length <= 150.
"""
#Difficulty: Easy
#99 / 99 test cases passed.
#Runtime: 24 ms
#Memory Usage: 13.9 MB

#Runtime: 24 ms, faster than 94.44% of Python3 online submissions for Goat Latin.
#Memory Usage: 13.9 MB, less than 42.39% of Python3 online submissions for Goat Latin.

class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')
        length = len(words)
        vowels = ('a', 'e', 'i', 'o', 'u')
        for i in range(length):
            if words[i][0].lower() in vowels:
                words[i] += 'ma'+ 'a' * (i + 1)
            else:
                words[i] = words[i][1:] + words[i][0] + 'ma'+ 'a' * (i + 1)
        return ' '.join(words)
