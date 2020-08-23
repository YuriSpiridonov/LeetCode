"""
    Implement the StreamChecker class as follows:
        - StreamChecker(words): Constructor, init the data structure with the 
          given words.
        - query(letter): returns true if and only if for some k >= 1, the last 
          k characters queried (in order from oldest to newest, including this 
          letter just queried) spell one of the words in the given list.

    Example:
    StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); 
                                                        // init the dictionary.
    streamChecker.query('a');          // return false
    streamChecker.query('b');          // return false
    streamChecker.query('c');          // return false
    streamChecker.query('d');          // return true, because 'cd' is in the 
                                       // wordlist
    streamChecker.query('e');          // return false
    streamChecker.query('f');          // return true, because 'f' is in the 
                                       // wordlist
    streamChecker.query('g');          // return false
    streamChecker.query('h');          // return false
    streamChecker.query('i');          // return false
    streamChecker.query('j');          // return false
    streamChecker.query('k');          // return false
    streamChecker.query('l');          // return true, because 'kl' is in the 
                                       // wordlist

    Note:
        - 1 <= words.length <= 2000
        - 1 <= words[i].length <= 2000
        - Words will only consist of lowercase English letters.
        - Queries will only consist of lowercase English letters.
        - The number of queries is at most 40000.
"""
#Difficulty: Hard
#17 / 17 test cases passed.
#Runtime: 1132 ms
#Memory Usage: 42.9 MB

#Runtime: 1132 ms, faster than 44.37% of Python3 online submissions for Stream of Characters.
#Memory Usage: 42.9 MB, less than 11.57% of Python3 online submissions for Stream of Characters.

class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

    def addWord(self, word):
        current = self
        i = len(word) - 1
        while i >= 0:
            index = ord(word[i]) - 97
            if not current.children[index]:
                current.children[index] = Trie()
            current = current.children[index]
            i -= 1
        current.is_word = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.stack = []
        self.words = Trie()
        for word in words:
            self.words.addWord(word)

    def query(self, letter: str) -> bool:
        self.stack.append(letter)
        current = self.words
        pop = len(self.stack) - 1
        while pop >= 0:    
            index = ord(self.stack[pop]) - 97
            if current.is_word:
                return True
            if not current.children[index]:
                return False
            current = current.children[index]
            pop -= 1
        return current.is_word


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
