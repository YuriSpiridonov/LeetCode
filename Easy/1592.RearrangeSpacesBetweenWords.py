"""
    You are given a string text of words that are placed among some number of 
    spaces. Each word consists of one or more lowercase English letters and are 
    separated by at least one space. It's guaranteed that text contains at 
    least one word.
    Rearrange the spaces so that there is an equal number of spaces between 
    every pair of adjacent words and that number is maximized. If you cannot 
    redistribute all the spaces equally, place the extra spaces at the end, 
    meaning the returned string should be the same length as text.

    Return the string after rearranging the spaces.

    Example:
    Input: text = "  this   is  a sentence "
    Output: "this   is   a   sentence"
    Explanation: There are a total of 9 spaces and 4 words. We can evenly divide 
                 the 9 spaces between the words: 9 / (4-1) = 3 spaces.

    Example:
    Input: text = " practice   makes   perfect"
    Output: "practice   makes   perfect "
    Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces 
    plus 1 extra space. We place this extra space at the end of the string.

    Example:
    Input: text = "hello   world"
    Output: "hello   world"

    Example:
    Input: text = "  walks  udp package   into  bar a"
    Output: "walks  udp  package  into  bar  a "

    Example:
    Input: text = "a"
    Output: "a"

    Constraints:
        - 1 <= text.length <= 100
        - text consists of lowercase English letters and ' '.
        - text contains at least one word.
"""
#Difficulty: Easy
#89 / 89 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.9 MB

#Runtime: 28 ms, faster than 87.57% of Python3 online submissions for Rearrange Spaces Between Words.
#Memory Usage: 13.9 MB, less than 29.42% of Python3 online submissions for Rearrange Spaces Between Words.

class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = tail = ''
        spaces_count = text.count(' ')
        words = [word for word in text.strip().split(' ') if word != '']
        words_count = len(words) - 1
        if words_count:
            spaces = ' ' * (spaces_count // words_count)
            tail = ' ' * (spaces_count % words_count)
        else:
            tail = ' ' * spaces_count
        return spaces.join(words) + tail
