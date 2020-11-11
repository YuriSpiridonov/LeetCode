"""
    Given the coordinates of four points in 2D space, return whether the four 
    points could construct a square.

    The coordinate (x,y) of a point is represented by an integer array with 
    two integers.

    Example:
    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: True

    Note:
        1. All the input integers are in the range [-10000, 10000].
        2. A valid square has four equal sides with positive length and four 
           equal angles (90-degree angles).
        3. Input points have no order.
"""
#Difficulty: Medium
#244 / 244 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14 MB

#Runtime: 36 ms, faster than 44.00% of Python3 online submissions for Valid Square.
#Memory Usage: 14 MB, less than 99.78% of Python3 online submissions for Valid Square.

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        result = {}
        for i in range(3):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i+1, 4):
                x2 = points[j][0]
                y2 = points[j][1]
                diagonal = ((x1-x2)**2 + (y1-y2)**2)**0.5
                if diagonal not in result:
                    result[diagonal] = 0
                result[diagonal] += 1
        return 2 in result.values() and 4 in result.values()
