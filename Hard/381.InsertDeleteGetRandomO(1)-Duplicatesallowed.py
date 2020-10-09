"""
    Design a data structure that supports all following operations in average 
    O(1) time.

    Note: Duplicate elements are allowed.
        1. insert(val): Inserts an item val to the collection.
        2. remove(val): Removes an item val from the collection if present.
        3. getRandom: Returns a random element from current collection of 
           elements. The probability of each element being returned is linearly 
           related to the number of same value the collection contains.

    Example:
        // Init an empty collection.
        RandomizedCollection collection = new RandomizedCollection();

        // Inserts 1 to the collection. Returns true as the collection did not 
        // contain 1.
        collection.insert(1);

        // Inserts another 1 to the collection. Returns false as the collection 
        // contained 1. Collection now contains [1,1].
        collection.insert(1);

        // Inserts 2 to the collection, returns true. Collection now contains 
        // [1,1,2].
        collection.insert(2);

        // getRandom should return 1 with the probability 2/3, and returns 2 
        // with the probability 1/3.
        collection.getRandom();

        // Removes 1 from the collection, returns true. Collection now contains 
        // [1,2].
        collection.remove(1);

        // getRandom should return 1 and 2 both equally likely.
        collection.getRandom();
"""
#Difficulty: Hard
#30 / 30 test cases passed.
#Runtime: 552 ms
#Memory Usage: 17.9 MB

#Runtime: 552 ms, faster than 7.10% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
#Memory Usage: 17.9 MB, less than 95.93% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.

import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.collection = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did 
        not already contain the specified element.
        """
        if val not in self.collection:
            self.collection.append(val)
            return True
        else:
            self.collection.append(val)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection 
        contained the specified element.
        """
        if val in self.collection:
            self.collection.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.collection)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
