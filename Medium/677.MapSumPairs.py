'''
    Implement the MapSum class:
        - MapSum() Initializes the MapSum object.
        - void insert(String key, int val) Inserts the key-val 
          pair into the map. If the key already existed, the 
          original key-value pair will be overridden to the 
          new one.
        - int sum(string prefix) Returns the sum of all the 
          pairs' value whose key starts with the prefix.

    Example:
    Input
            ["MapSum", "insert", "sum", "insert", "sum"]
            [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
    Output
            [null, null, 3, null, 5]
    Explanation
                MapSum mapSum = new MapSum();
                mapSum.insert("apple", 3);  
                mapSum.sum("ap");           // return 3 
                                            // (apple = 3)
                mapSum.insert("app", 2);    
                mapSum.sum("ap");           // return 5 
                                            // (apple + app = 3 + 2 = 5)

    Constraints:
        - 1 <= key.length, prefix.length <= 50
        - key and prefix consist of only lowercase English 
          letters.
        - 1 <= val <= 1000
        - At most 50 calls will be made to insert and sum.
'''
#Difficulty: Medium
#34 / 34 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.3 MB

#Runtime: 28 ms, faster than 86.01% of Python3 online submissions for Map Sum Pairs.
#Memory Usage: 14.3 MB, less than 34.50% of Python3 online submissions for Map Sum Pairs.

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.letters = [None] * 26
        self.value = 0

    def insert(self, key: str, val: int) -> None:
        current = self
        i = 0
        while i < len(key):
            index = ord(key[i]) - 97
            if not current.letters[index]:
                current.letters[index] = MapSum()
            current = current.letters[index]
            i += 1
        current.value = val

    def sum(self, prefix: str) -> int:
        current = self
        result = 0
        queue = []
        queue.extend(list(prefix))
        while queue and current:  
            current = current.letters[ord(queue.pop(0)) - 97]
        queue.append(current)
        while queue and current:
            current = queue.pop(0)
            queue.extend([letter for letter in current.letters if letter])
            result += current.value
        return result


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
