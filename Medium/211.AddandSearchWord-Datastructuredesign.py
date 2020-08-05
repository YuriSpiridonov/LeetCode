"""
    Design a data structure that supports the following two operations:

        void addWord(word)
        bool search(word)
    search(word) can search a literal word or a regular expression string 
    containing only letters a-z or .. A . means it can represent any one letter.

    Example:
        addWord("bad")
        addWord("dad")
        addWord("mad")
        search("pad") -> false
        search("bad") -> true
        search(".ad") -> true
        search("b..") -> true

    Note:
        You may assume that all words are consist of lowercase letters a-z.
"""
#Difficulty: Medium
#13 / 13 test cases passed.
#Runtime: 588 ms
#Memory Usage: 30.5 MB

#Runtime: 588 ms, faster than 12.54% of Python3 online submissions for Add and Search Word - Data structure design.
#Memory Usage: 30.5 MB, less than 9.69% of Python3 online submissions for Add and Search Word - Data structure design.

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.is_word = False

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self
        for char in word:
            index = ord(char) - ord('a')
            if not current.children[index]:
                current.children[index] = WordDictionary()
            current = current.children[index]
        current.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the 
        dot character '.' to represent any one letter.
        """
        current = self
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if word[i] == '.':
                for char in current.children:
                    if char and char.search(word[i+1:]):
                        return True
                return False
            if not current.children[index]:
                return False
            current = current.children[index]
        return current and current.is_word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
