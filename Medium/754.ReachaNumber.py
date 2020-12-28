'''
    You are standing at position 0 on an infinite number line. 
    There is a goal at position target.

    On each move, you can either go left or right. During the 
    n-th move (starting from 1), you take n steps.

    Return the minimum number of steps required to reach the 
    destination.

    Example:
    Input: target = 3
    Output: 2
    Explanation:
                On the first move we step from 0 to 1.
                On the second step we step from 1 to 3.

    Example:
    Input: target = 2
    Output: 3
    Explanation:
                On the first move we step from 0 to 1.
                On the second move we step  from 1 to -1.
                On the third move we step from -1 to 2.

    Note:
        - target will be a non-zero integer in the range 
          [-10^9, 10^9].
'''
#Difficulty: Medium
#73 / 73 test cases passed.
#Runtime: 188 ms
#Memory Usage: 14.3 MB

#Runtime: 188 ms, faster than 5.48% of Python3 online submissions for Reach a Number.
#Memory Usage: 14.3 MB, less than 27.40% of Python3 online submissions for Reach a Number.

class Solution:
    def reachNumber(self, target: int) -> int:
        step = 0
        target = abs(target)
        while step <= 1 + target:
            step += 1
            number = (step * (step-1)) // 2
            if number >= target and not (target-number) % 2:
                return step-1
