'''
    Given an Iterator class interface with methods: next() 
    and hasNext(), design and implement a PeekingIterator 
    that support the peek() operation -- it essentially 
    peek() at the element that will be returned by the next 
    call to next().

    Example:
    Assume that the iterator is initialized to the beginning 
    of the list: [1,2,3].

    - Call next() gets you 1, the first element in the list.
    - Now you call peek() and it returns 2, the next element. 
      Calling next() after that still return 2. 
    - You call next() the final time and it returns 3, the 
      last element. 
    - Calling hasNext() after that should return false.

    Follow up: How would you extend your design to be 
               generic and work with all types, not just 
               integer?
'''
#Difficulty: Medium
#13 / 13 test cases passed.
#Runtime: 44 ms
#Memory Usage: 14.6 MB

#Runtime: 44 ms, faster than 8.09% of Python3 online submissions for Peeking Iterator.
#Memory Usage: 14.6 MB, less than 28.50% of Python3 online submissions for Peeking Iterator.

# Below is the interface for Iterator, which is already 
# defined for you.
#
# class Iterator:
#
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning 
#         of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.cache = False
        self.iterator = iterator
        self.val = None

    def peek(self):
        """
        Returns the next element in the iteration without 
        advancing the iterator.
        :rtype: int
        """
        if not self.cache:
            self.cache = True
            self.val = self.iterator.next()
        return self.val

    def next(self):
        """
        :rtype: int
        """
        if not self.cache:
            self.val = self.peek()
        self.cache = False
        return self.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iterator.hasNext() or self.cache


# Your PeekingIterator object will be instantiated and 
# called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not 
#                           advance the iterator.
#     iter.next()         # Should return the same value 
#                           as [val].
