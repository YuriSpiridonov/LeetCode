"""
    Median is the middle value in an ordered integer list. If the size of the 
    list is even, there is no middle value. So the median is the mean of the 
    two middle value.

    For example,
    [2,3,4], the median is 3
    [2,3], the median is (2 + 3) / 2 = 2.5

    Design a data structure that supports the following two operations:
        - void addNum(int num) - Add a integer number from the data stream to 
          the data structure.
        - double findMedian() - Return the median of all elements so far.

    Example:

        addNum(1)
        addNum(2)
        findMedian() -> 1.5
        addNum(3) 
        findMedian() -> 2

    Follow up:
        1. If all integer numbers from the stream are between 0 and 100, how 
           would you optimize it?
        2. If 99% of all integer numbers from the stream are between 0 and 100, 
           how would you optimize it?
"""
#Difficulty: Hard
#18 / 18 test cases passed.
#Runtime: 1252 ms
#Memory Usage: 24.9 MB

#Runtime: 1252 ms, faster than 12.48% of Python3 online submissions for Find Median from Data Stream.
#Memory Usage: 24.9 MB, less than 61.00% of Python3 online submissions for Find Median from Data Stream.

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.db = []

    def addNum(self, num: int) -> None:
        self.db.append(num)

    def findMedian(self) -> float:
        length = len(self.db)
        self.db.sort()
        if length % 2:
            return self.db[length//2]
        else:
            return (self.db[-1+length//2] + self.db[length//2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
