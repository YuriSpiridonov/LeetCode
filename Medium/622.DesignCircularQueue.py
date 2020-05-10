"""
    Design your implementation of the circular queue. The circular queue is a 
    linear data structure in which the operations are performed based on FIFO 
    (First In First Out) principle and the last position is connected back to 
    the first position to make a circle. It is also called "Ring Buffer".
    
    One of the benefits of the circular queue is that we can make use of the 
    spaces in front of the queue. In a normal queue, once the queue becomes 
    full, we cannot insert the next element even if there is a space in front 
    of the queue. But using the circular queue, we can use the space to store 
    new values.
    
    Your implementation should support following operations:
    
    MyCircularQueue(k): Constructor, set the size of the queue to be k.
    Front: Get the front item from the queue. If the queue is empty, return -1.
    Rear: Get the last item from the queue. If the queue is empty, return -1.
    enQueue(value): Insert an element into the circular queue. Return true if 
    the operation is successful.
    deQueue(): Delete an element from the circular queue. Return true if the 
    operation is successful.
    isEmpty(): Checks whether the circular queue is empty or not.
    isFull(): Checks whether the circular queue is full or not.
     
    
    Example:
    MyCircularQueue circularQueue = new MyCircularQueue(3); 
                                                        // set the size to be 3
    circularQueue.enQueue(1);  // return true
    circularQueue.enQueue(2);  // return true
    circularQueue.enQueue(3);  // return true
    circularQueue.enQueue(4);  // return false, the queue is full
    circularQueue.Rear();  // return 3
    circularQueue.isFull();  // return true
    circularQueue.deQueue();  // return true
    circularQueue.enQueue(4);  // return true
    circularQueue.Rear();  // return 4
     
    Note:
    All values will be in the range of [0, 1000].
    The number of operations will be in the range of [1, 1000].
    Please do not use the built-in Queue library.
"""
#Difficulty: Medium
#52 / 52 test cases passed.
#Runtime: 100 ms
#Memory Usage: 14 MB

#Runtime: 100 ms, faster than 9.41% of Python3 online submissions for Design Circular Queue.
#Memory Usage: 14 MB, less than 5.26% of Python3 online submissions for Design Circular Queue.

class MyCircularQueue: # First time. Solved by myself without theory
    def __init__(self, k: int):
        self.k = k - 1
        self.front = self.rear = -1
        self.queue = [None] * k

    def enQueue(self, value: int) -> bool:
        r = False
        if self.isFull():
            return r
        if self.rear == -1:
            self.front += 1
            self.rear += 1
            self.queue[self.rear] = value
            r = True
        elif self.rear != self.k:
            self.rear += 1
            self.queue[self.rear] = value
            r = True
        elif self.rear == self.k and not self.isFull():
            self.rear = 0
            self.queue[self.rear] = value
            r = True
        return r

    def deQueue(self) -> bool:
        r = False
        if self.front == -1 or self.isEmpty():
            return r
        elif self.front != self.k:
            self.queue[self.front] = None
            self.front += 1
            if self.isEmpty():
                self.front = -1
                self.rear = -1
            r = True
        elif self.front == self.k and not self.isEmpty():
            self.queue[self.front] = None
            self.front = 0
            r = True
        return r

    def Front(self) -> int:
        if self.isEmpty():
            self.front = -1
            self.rear = -1
            return self.front
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            self.front = -1
            self.rear = -1
            return self.rear
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return True if self.queue.count(None) == self.k + 1 else False

    def isFull(self) -> bool:
        return True if None not in self.queue else False
