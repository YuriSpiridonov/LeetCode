"""
    We are given an array asteroids of integers representing asteroids in a 
    row.
    For each asteroid, the absolute value represents its size, and the sign 
    represents its direction (positive meaning right, negative meaning left). 
    Each asteroid moves at the same speed.
    Find out the state of the asteroids after all collisions. If two asteroids 
    meet, the smaller one will explode. If both are the same size, both will 
    explode. Two asteroids moving in the same direction will never meet.

    Example:
    Input: asteroids = [5,10,-5]
    Output: [5,10]
    Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never 
                 collide.

    Example:
    Input: asteroids = [8,-8]
    Output: []
    Explanation: The 8 and -8 collide exploding each other.

    Example:
    Input: asteroids = [10,2,-5]
    Output: [10]
    Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide 
                 resulting in 10.

    Example:
    Input: asteroids = [-2,-1,1,2]
    Output: [-2,-1,1,2]
    Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving 
                 right. Asteroids moving the same direction never meet, so no 
                 asteroids will meet each other.

    Constraints:
        - 1 <= asteroids <= 10**4
        - -1000 <= asteroids[i] <= 1000
        - asteroids[i] != 0
"""
#Difficulty: Medium
#275 / 275 test cases passed.
#Runtime: 84 ms
#Memory Usage: 15.1 MB

#Runtime: 84 ms, faster than 98.87% of Python3 online submissions for Asteroid Collision.
#Memory Usage: 15.1 MB, less than 99.31% of Python3 online submissions for Asteroid Collision.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        result = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] < abs(asteroid):
                    stack.pop()
                if stack and stack[-1] == abs(asteroid):
                    stack.pop()
                    continue
                if not stack:
                    result.append(asteroid)
        if stack:
            result.extend(stack)
        return result
