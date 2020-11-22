"""
    International Morse Code defines a standard encoding where each letter is 
    mapped to a series of dots and dashes, as follows: "a" maps to ".-", 
    "b" maps to "-...", "c" maps to "-.-.", and so on.

    For convenience, the full table for the 26 letters of the English alphabet 
    is given below:
        [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
        ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
        ".--","-..-","-.--","--.."]
    
    Now, given a list of words, each word can be written as a concatenation of 
    the Morse code of each letter. For example, "cab" can be written as 
    "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). 
    We'll call such a concatenation, the transformation of a word.

    Return the number of different transformations among all words we have.

    Example:
    Input: words = ["gin", "zen", "gig", "msg"]
    Output: 2
    Explanation: 
                 The transformation of each word is:
                 "gin" -> "--...-."
                 "zen" -> "--...-."
                 "gig" -> "--...--."
                 "msg" -> "--...--."
                 There are 2 different transformations, "--...-." 
                                                             and "--...--.".

    Note:
        - The length of words will be at most 100.
        - Each words[i] will have length in range [1, 12].
        - words[i] will only consist of lowercase letters.
"""
#Difficulty: Easy
#83 / 83 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.3 MB

#Runtime: 32 ms, faster than 78.35% of Python3 online submissions for Unique Morse Code Words.
#Memory Usage: 14.3 MB, less than 11.47% of Python3 online submissions for Unique Morse Code Words.

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = {}
        words = set(words)
        for word in words:
            for char in word:
                if word not in transformations:
                    transformations[word] = ''
                transformations[word] += morse[ord(char)-97]
        return len(set(transformations.values()))
