"""
    There is a special square room with mirrors on each of the four walls. 
    Except for the southwest corner, there are receptors on each of the
    remaining corners, numbered 0, 1, and 2.

    The square room has walls of length p, and a laser ray from the southwest 
    corner first meets the east wall at a distance q from the 0th receptor.

    Return the number of the receptor that the ray meets first.
    (It is guaranteed that the ray will meet a receptor eventually.)

    Example:
    Input: p = 2, q = 1
    Output: 2
    Explanation: The ray meets receptor 2 the first time it gets reflected 
                 back to the left wall.

    Note:
        1. 1 <= p <= 1000
        2. 0 <= q <= p
"""
#Difficulty: Medium
#69 / 69 test cases passed.
#Runtime: 20 ms
#Memory Usage: 14.2 MB

#Runtime: 20 ms, faster than 98.25% of Python3 online submissions for Mirror Reflection.
#Memory Usage: 14.2 MB, less than 30.88% of Python3 online submissions for Mirror Reflection.

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        path = 0
        right = True
        go_up = True
        while True:
            if go_up:
                path += q
            else:
                path -= q
            if path == 0:
                return 0
            elif path == p:
                return 1 if right else 2
            if path > p:
                go_up = not go_up
                path = 2 * p - path
            elif path < 0:
                go_up = not go_up
                path = - path
            right = not right
