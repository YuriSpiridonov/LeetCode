"""
    Design a HashMap without using any built-in hash table libraries.

    To be specific, your design should include these functions:
        - put(key, value) : Insert a (key, value) pair into the HashMap. 
          If the value already exists in the HashMap, update the value.
        - get(key): Returns the value to which the specified key is mapped, 
          or -1 if this map contains no mapping for the key.
        - remove(key) : Remove the mapping for the value key if this map 
          contains the mapping for the key.

    Example:
    MyHashMap hashMap = new MyHashMap();
    hashMap.put(1, 1);          
    hashMap.put(2, 2);         
    hashMap.get(1);             // returns 1
    hashMap.get(3);             // returns -1 (not found)
    hashMap.put(2, 1);          // update the existing value
    hashMap.get(2);             // returns 1 
    hashMap.remove(2);          // remove the mapping for 2
    hashMap.get(2);             // returns -1 (not found) 

    Note:
        - All keys and values will be in the range of [0, 1000000].
        - The number of operations will be in the range of [1, 10000].
        - Please do not use the built-in HashMap library.
"""
#Difficulty: Easy
#33 / 33 test cases passed.
#Runtime: 352 ms
#Memory Usage: 39.1 MB

#Runtime: 352 ms, faster than 41.67% of Python3 online submissions for Design HashMap.
#Memory Usage: 39.1 MB, less than 5.70% of Python3 online submissions for Design HashMap.

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.db = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.db[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this 
        map contains no mapping for the key
        """
        return self.db[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a 
        mapping for the key
        """
        self.db[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
