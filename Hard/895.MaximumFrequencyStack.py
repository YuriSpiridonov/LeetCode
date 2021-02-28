'''
    Implement FreqStack, a class which simulates the operation 
    of a stack-like data structure.

    FreqStack has two functions:

        - push(int x), which pushes an integer x onto the 
          stack.
        - pop(), which removes and returns the most frequent 
          element in the stack.
            = If there is a tie for most frequent element, 
              the element closest to the top of the stack is 
              removed and returned.

    Example:
    Input: 
    ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
    [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
    Output: [null,null,null,null,null,null,null,5,7,5,4]
    Explanation:
                 After making six .push operations, the stack 
                 is [5,7,5,7,4,5] from bottom to top.  Then:

                 pop() -> returns 5, as 5 is the most frequent.
                 The stack becomes [5,7,5,7,4].

                 pop() -> returns 7, as 5 and 7 is the most 
                 frequent, but 7 is closest to the top.
                 The stack becomes [5,7,5,4].

                 pop() -> returns 5.
                 The stack becomes [5,7,4].

                 pop() -> returns 4.
                 The stack becomes [5,7].

    Note:
        - Calls to FreqStack.push(int x) will be such that 
          0 <= x <= 10^9.
        - It is guaranteed that FreqStack.pop() won't be 
          called if the stack has zero elements.
        - The total number of FreqStack.push calls will not 
          exceed 10000 in a single test case.
        - The total number of FreqStack.pop calls will not 
          exceed 10000 in a single test case.
        - The total number of FreqStack.push and FreqStack.pop 
          calls will not exceed 150000 across all test cases.
'''
#Dfficulty: Hard
#37 / 37 test cases passed.
#Runtime: 9076 ms
#Memory Usage: 22.3 MB

#Runtime: 9076 ms, faster than 5.05% of Python3 online submissions for Maximum Frequency Stack.
#Memory Usage: 22.3 MB, less than 64.04% of Python3 online submissions for Maximum Frequency Stack.

class FreqStack:

    def __init__(self):
        self.stack = []
        self.count = {}

    def push(self, x: int) -> None:
        if x not in self.count:
            self.count[x] = 1
        else:
            self.count[x] += 1
        self.stack.append((x, self.count[x]))

    def pop(self) -> int:
        max_count = max(self.count, key = self.count.get)
        length = len(self.stack)
        while length:
            length -= 1
            if self.stack[length][1] == self.count[max_count]:
                self.count[max_count] -= 1
                return self.stack.pop(length)[0]        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()