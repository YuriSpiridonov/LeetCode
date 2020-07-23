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
#Runtime: 328 ms
#Memory Usage: 24.9 MB

#Runtime: 328 ms, faster than 31.53% of Python3 online submissions for Find Median from Data Stream.
#Memory Usage: 24.9 MB, less than 69.30% of Python3 online submissions for Find Median from Data Stream.

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1
        if not self.array:
            self.array.append(num)
        else:
            self.binarySearch(num)

    def binarySearch(self, num):
        l = 0
        r = len(self.array) - 1
        while l <= r:
            m = (l + r) // 2
            if  self.array[m-1] <= num <= self.array[m]:
                return self.array.insert(m, num)
            elif num > self.array[m]:
                l = m + 1
            else:
                r = m - 1
        return self.array.insert(l, num)

    def findMedian(self) -> float:
        if self.length % 2:
            return self.array[self.length//2]
        else:
            return (self.array[-1+self.length//2] + self.array[self.length//2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
