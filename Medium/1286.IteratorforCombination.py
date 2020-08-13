"""
    Design an Iterator class, which has:
        - A constructor that takes a string characters of sorted distinct 
          lowercase English letters and a number combinationLength as arguments.
        - A function next() that returns the next combination of length 
          combinationLength in lexicographical order.
        - A function hasNext() that returns True if and only if there exists a 
          next combination.

    Example:
    CombinationIterator iterator = new CombinationIterator("abc", 2); 
                                                       // creates the iterator.
    iterator.next(); // returns "ab"
    iterator.hasNext(); // returns true
    iterator.next(); // returns "ac"
    iterator.hasNext(); // returns true
    iterator.next(); // returns "bc"
    iterator.hasNext(); // returns false

    Constraints:
        - 1 <= combinationLength <= characters.length <= 15
        - There will be at most 10^4 function calls per test.
        - It's guaranteed that all calls of the function next are valid.
"""
#Difficulty: Medium
#16 / 16 test cases passed.
#Runtime: 48 ms
#Memory Usage: 16.4 MB

#Runtime: 48 ms, faster than 93.97% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
#Memory Usage: 16.4 MB, less than 13.23% of Python3 online submissions for Maximum Points You Can Obtain from Cards.

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.index = -1
        self.combinations = []
        for combination in itertools.combinations(characters, combinationLength):
            self.combinations.append(''.join(combination))
        self.size = len(self.combinations) - 1

    def next(self) -> str:
        self.index += 1
        return self.combinations[self.index]

    def hasNext(self) -> bool:
        if self.index < self.size:
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
