"""
    There are some spherical balloons spread in two-dimensional space. For each 
    balloon, provided input is the start and end coordinates of the horizontal 
    diameter. Since it's horizontal, y-coordinates don't matter, and hence the 
    x-coordinates of start and end of the diameter suffice. The start is always 
    smaller than the end.

    An arrow can be shot up exactly vertically from different points along the 
    x-axis. A balloon with x(start) and x(end) bursts by an arrow shot at x if 
    x(start) ≤ x ≤ x(end). There is no limit to the number of arrows that can 
    be shot. An arrow once shot keeps traveling up infinitely.

    Given an array points where points[i] = [x(start), x(end)], return the 
    minimum number of arrows that must be shot to burst all balloons.

    Example:
    Input: points = [[10,16],[2,8],[1,6],[7,12]]
    Output: 2
    Explanation: One way is to shoot one arrow for example at x = 6 
                 (bursting the balloons [2,8] and [1,6]) and another arrow at 
                 x = 11 (bursting the other two balloons).

    Example:
    Input: points = [[1,2],[3,4],[5,6],[7,8]]
    Output: 4

    Example:
    Input: points = [[1,2],[2,3],[3,4],[4,5]]
    Output: 2

    Example:
    Input: points = [[1,2]]
    Output: 1

    Example:
    Input: points = [[2,3],[2,3]]
    Output: 1

    Constraints:
        - 0 <= points.length <= 10**4
        - points.length == 2
        - -2**31 <= xstart < xend <= 2**31 - 1
"""
#Difficulty: Medium
#45 / 45 test cases passed.
#Runtime: 424 ms
#Memory Usage: 18.4 MB

#Runtime: 424 ms, faster than 86.48% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
#Memory Usage: 18.4 MB, less than 97.86% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        i = 0
        length = len(points)
        points.sort(key=lambda points : points[1])
        while True:
            j = i + 1
            if j >= length:
                return length
            if points[j][0] <= points[i][1]:
                points.pop(j)
                i -= 1
                length -= 1
            i += 1
