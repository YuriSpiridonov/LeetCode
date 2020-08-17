"""
    Given two sequences pushed and popped with distinct values, return true if 
    and only if this could have been the result of a sequence of push and pop 
    operations on an initially empty stack.

    Example:
    Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    Output: true
    Explanation: We might do the following sequence:
                 push(1), push(2), push(3), push(4), pop() -> 4,
                 push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

    Example:
    Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
    Output: false
    Explanation: 1 cannot be popped before 2.

    Constraints:
        - 0 <= pushed.length == popped.length <= 1000
        - 0 <= pushed[i], popped[i] < 1000
        - pushed is a permutation of popped.
        - pushed and popped have distinct values.
"""
#Difficulty: Medium
#152 / 152 test cases passed.
#Runtime: 64 ms
#Memory Usage: 13.9 MB

#Runtime: 64 ms, faster than 98.89% of Python3 online submissions for Validate Stack Sequences.
#Memory Usage: 13.9 MB, less than 69.26% of Python3 online submissions for Validate Stack Sequences.

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for push in pushed:
            stack.append(push)
            while stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
                if not stack:
                    break
        return not stack
