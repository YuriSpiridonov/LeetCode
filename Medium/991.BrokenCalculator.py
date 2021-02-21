'''
    On a broken calculator that has a number showing on its 
    display, we can perform two operations:
        - Double: Multiply the number on the display by 2, or;
        - Decrement: Subtract 1 from the number on the display.

    Initially, the calculator is displaying the number X.

    Return the minimum number of operations needed to display 
    the number Y.

    Example:
    Input: X = 2, Y = 3
    Output: 2
    Explanation: Use double operation and then decrement 
                 operation {2 -> 4 -> 3}.

    Example:
    Input: X = 5, Y = 8
    Output: 2
    Explanation: Use decrement and then double {5 -> 4 -> 8}.

    Example:
    Input: X = 3, Y = 10
    Output: 3
    Explanation: Use double, decrement and double 
                 {3 -> 6 -> 5 -> 10}.

    Example:
    Input: X = 1024, Y = 1
    Output: 1023
    Explanation: Use decrement operations 1023 times.

    Note:
        1. 1 <= X <= 10^9
        2. 1 <= Y <= 10^9
'''
#Dificulty: Medium
#84 / 84 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.2 MB

#Runtime: 28 ms, faster than 86.05% of Python3 online submissions for Broken Calculator.
#Memory Usage: 14.2 MB, less than 72.43% of Python3 online submissions for Broken Calculator.

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        operations = 0
        queue = [Y]
        while queue:
            Y = queue.pop(0)

            if not Y % 2:
                queue.append(Y//2)
            else:
                queue.append(Y+1)

            if X >= Y:
                return operations + X - Y

            operations += 1