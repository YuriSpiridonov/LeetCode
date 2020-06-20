"""
    Design your implementation of the circular double-ended queue (deque).
    Your implementation should support following operations:
    
        - MyCircularDeque(k): Constructor, set the size of the deque to be k.
        - insertFront(): Adds an item at the front of Deque. Return true if 
          the operation is successful.
        - insertLast(): Adds an item at the rear of Deque. Return true if the 
          operation is successful.
        - deleteFront(): Deletes an item from the front of Deque. Return true 
          if the operation is successful.
        - deleteLast(): Deletes an item from the rear of Deque. Return true 
          if the operation is successful.
        - getFront(): Gets the front item from the Deque. If the deque is 
          empty, return -1.
        - getRear(): Gets the last item from Deque. If the deque is empty, 
          return -1.
        - isEmpty(): Checks whether Deque is empty or not. 
        - isFull(): Checks whether Deque is full or not.

    Example:
    MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
    circularDeque.insertLast(1);			// return true
    circularDeque.insertLast(2);			// return true
    circularDeque.insertFront(3);			// return true
    circularDeque.insertFront(4);			// return false, the queue is full
    circularDeque.getRear();  			    // return 2
    circularDeque.isFull();				    // return true
    circularDeque.deleteLast();			    // return true
    circularDeque.insertFront(4);			// return true
    circularDeque.getFront();			    // return 4

    Note:
        - All values will be in the range of [0, 1000].
        - The number of operations will be in the range of [1, 1000].
        - Please do not use the built-in Deque library.
"""
#Difficulty: Medium
#51 / 51 test cases passed.
#Runtime: 60 ms
#Memory Usage: 14.1 MB

#Runtime: 60 ms, faster than 99.45% of Python3 online submissions for Design Circular Deque.
#Memory Usage: 14.1 MB, less than 79.26% of Python3 online submissions for Design Circular Deque.

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is 
        successful.
        """
        if not self.isFull():
            self.deque.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is 
        successful.
        """
        if not self.isFull():
            self.deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation 
        is successful.
        """
        if not self.isEmpty():
            self.deque.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation 
        is successful.
        """
        if not self.isEmpty():
            self.deque.pop(-1)
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.deque[0]
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.deque[-1]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not self.deque

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.deque) == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
