"""
    Implement a trie with insert, search, and startsWith methods.

    Example:
            Trie trie = new Trie();

            trie.insert("apple");
            trie.search("apple");   // returns true
            trie.search("app");     // returns false
            trie.startsWith("app"); // returns true
            trie.insert("app");   
            trie.search("app");     // returns true

    Note:
        - You may assume that all inputs are consist of lowercase letters a-z.
        - All inputs are guaranteed to be non-empty strings.
"""
#Difficulty: Medium
#15 / 15 test cases passed.
#Runtime: 328 ms
#Memory Usage: 32.3 MB

#Runtime: 328 ms, faster than 16.29% of Python3 online submissions for Implement Trie (Prefix Tree).
#Memory Usage: 32.3 MB, less than 25.53% of Python3 online submissions for Implement Trie (Prefix Tree).

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        length = len(word)
        count = 0
        isWord = False
        current = self.root
        for i in range(1, length+1):
            count += 1
            if count == length:
                isWord = True
            if word[:i] not in current:
                current[word[:i]] = {word[:i] : isWord}
                current = current[word[:i]]
            else:
                current = current[word[:i]]
        current[word[:i]] = isWord

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        length = len(word)
        current = self.root
        for i in range(1, length+1):
            if word[:i] not in current:
                return False
            current = current[word[:i]]
        return current[word[:i]]

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        length = len(prefix)
        current = self.root
        for i in range(1, length+1):
            if prefix[:i] not in current:
                return False
            current = current[prefix[:i]]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
