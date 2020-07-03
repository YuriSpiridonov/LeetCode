"""
    Implement a data structure supporting the following operations:
        1. Inc(Key) - Inserts a new key with value 1. Or increments an existing 
           key by 1. Key is guaranteed to be a non-empty string.
        2. Dec(Key) - If Key's value is 1, remove it from the data structure. 
           Otherwise decrements an existing key by 1. If the key does not exist, 
           this function does nothing. Key is guaranteed to be a non-empty 
           string.
        3. GetMaxKey() - Returns one of the keys with maximal value. If no 
           element exists, return an empty string "".
        4. GetMinKey() - Returns one of the keys with minimal value. If no 
           element exists, return an empty string "".

    Challenge: Perform all these in O(1) time complexity.
"""
#Difficulty: Hard
#15 / 15 test cases passed.
#Runtime: 80 ms
#Memory Usage: 17.9 MB

#Runtime: 80 ms, faster than 94.87% of Python3 online submissions for All O`one Data Structure.
#Memory Usage: 17.9 MB, less than 98.39% of Python3 online submissions for All O`one Data Structure.

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.db = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.db.keys():
            self.db[key] += 1
        else:
            self.db[key] = 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if not self.db:
            return
        elif self.db[key] > 1:
            if key in self.db.keys():
                self.db[key] -= 1
        else:
            del self.db[key]
    
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return max(self.db, key=self.db.get) if self.db else ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return min(self.db, key=self.db.get) if self.db else ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
