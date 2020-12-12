'''
    Design a queue that supports push and pop operations in the front, 
    middle, and back.

    Implement the FrontMiddleBack class:
        - FrontMiddleBack() Initializes the queue.
        - void pushFront(int val) Adds val to the front of the queue.
        - void pushMiddle(int val) Adds val to the middle of the queue.
        - void pushBack(int val) Adds val to the back of the queue.
        - int popFront() Removes the front element of the queue and 
          returns it. If the queue is empty, return -1.
        - int popMiddle() Removes the middle element of the queue 
          and returns it. If the queue is empty, return -1.
        - int popBack() Removes the back element of the queue and 
          returns it. If the queue is empty, return -1.

    Notice that when there are two middle position choices, the 
    operation is performed on the frontmost middle position choice. 
    For example:
        - Pushing 6 into the middle of [1, 2, 3, 4, 5] results 
          in [1, 2, 6, 3, 4, 5].
        - Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and 
          results in [1, 2, 4, 5, 6].

    Example:

    Input:
    ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", 
    "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", 
    "popFront"]
    [[], [1], [2], [3], [4], [], [], [], [], []]
    Output:
    [null, null, null, null, null, 1, 3, 4, 2, -1]

    Explanation:
                FrontMiddleBackQueue q = new FrontMiddleBackQueue();
                q.pushFront(1);   // [1]
                q.pushBack(2);    // [1, 2]
                q.pushMiddle(3);  // [1, 3, 2]
                q.pushMiddle(4);  // [1, 4, 3, 2]
                q.popFront();     // return 1 -> [4, 3, 2]
                q.popMiddle();    // return 3 -> [4, 2]
                q.popMiddle();    // return 4 -> [2]
                q.popBack();      // return 2 -> []
                q.popFront();     // return -1 -> [] (The queue is empty)

    Constraints:
        - 1 <= val <= 10^9
        - At most 1000 calls will be made to pushFront, pushMiddle, 
          pushBack, popFront, popMiddle, and popBack.
'''
#Difficulty: Medium
#94 / 94 test cases passed.
#Runtime: 72 ms
#Memory Usage: 14.9 MB

#Runtime: 72 ms, faster than 80.76% of Python3 online submissions for Design Front Middle Back Queue.
#Memory Usage: 14.9 MB, less than 52.60% of Python3 online submissions for Design Front Middle Back Queue.

class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []
        self.length = 0

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)
        self.length += 1

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(self.length//2, val)
        self.length += 1

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        self.length += 1

    def popFront(self) -> int:
        if self.length:
            self.length -= 1
            return self.queue.pop(0)
        return -1

    def popMiddle(self) -> int:
        if self.length:
            self.length -= 1
            return self.queue.pop(self.length//2)
        return -1

    def popBack(self) -> int:
        if self.length:
            self.length -= 1
            return self.queue.pop()
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
