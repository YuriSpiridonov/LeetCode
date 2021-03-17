'''
    Given the radius and x-y positions of the center of a 
    circle, write a function randPoint which generates a 
    uniform random point in the circle.

    Note:
        1. input and output values are in floating-point.
        2. radius and x-y position of the center of the 
           circle is passed into the class constructor.
        3. a point on the circumference of the circle is 
           considered to be in the circle.
        4. randPoint returns a size 2 array containing 
           x-position and y-position of the random point, 
           in that order.

    Example:
    Input: 
    ["Solution","randPoint","randPoint","randPoint"]
    [[1,0,0],[],[],[]]
    Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

    Example:
    Input: 
    ["Solution","randPoint","randPoint","randPoint"]
    [[10,5,-7.5],[],[],[]]
    Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

    Explanation of Input Syntax:
    The input is two lists: the subroutines called and their 
    arguments. Solution's constructor has three arguments, 
    the radius, x-position of the center, and y-position of 
    the center of the circle. randPoint has no arguments. 
    Arguments are always wrapped with a list, even if there 
    aren't any.
'''
#Difficulty: Medium
#8 / 8 test cases passed.
#Runtime: 140 ms
#Memory Usage: 24.6 MB

#Runtime: 140 ms, faster than 74.16% of Python3 online submissions for Generate Random Point in a Circle.
#Memory Usage: 24.6 MB, less than 20.10% of Python3 online submissions for Generate Random Point in a Circle.

import math
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        angle = random.uniform(0, 360)
        radius = self.radius * math.sqrt(random.random())
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        return [self.x_center + x, self.y_center + y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()