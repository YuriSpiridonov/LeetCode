'''
    You are given a nested list of integers nestedList. 
    Each element is either an integer or a list whose 
    elements may also be integers or other lists. Implement 
    an iterator to flatten it.

    Implement the NestedIterator class:
        - NestedIterator(List<NestedInteger> nestedList) I
          nitializes the iterator with the nested list 
          nestedList.
        - int next() Returns the next integer in the nested 
          list.
        - boolean hasNext() Returns true if there are still 
          some integers in the nested list and false 
          otherwise.

    Example:
    Input: nestedList = [[1,1],2,[1,1]]
    Output: [1,1,2,1,1]
    Explanation: By calling next repeatedly until hasNext 
                 returns false, the order of elements 
                 returned by next should be: [1,1,2,1,1].

    Example:
    Input: nestedList = [1,[4,[6]]]
    Output: [1,4,6]
    Explanation: By calling next repeatedly until hasNext 
                 returns false, the order of elements 
                 returned by next should be: [1,4,6].

    Constraints:
        - 1 <= nestedList.length <= 500
        - The values of the integers in the nested list is 
          in the range [-10^6, 10^6].
'''
#Difficulty: Medium
#43 / 43 test cases passed.
#Runtime: 92 ms
#Memory Usage: 17.6 MB

#Runtime: 92 ms, faster than 6.19% of Python3 online submissions for Flatten Nested List Iterator.
#Memory Usage: 17.6 MB, less than 71.64% of Python3 online submissions for Flatten Nested List Iterator.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single 
#        integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger 
#        holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger 
#        holds, if it holds a nested list
#        Return None if this NestedInteger holds a single 
#        integer
#        """

class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.queue = []
        self.iterator(nestedList)

    def next(self) -> int:
        return self.queue.pop(0)

    def hasNext(self) -> bool:
        return self.queue

    def iterator(self, nestedList):
        for value in nestedList:
            if value.isInteger():
                self.queue.append(value)
            if value.getList():
                self.iterator(value.getList())


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())