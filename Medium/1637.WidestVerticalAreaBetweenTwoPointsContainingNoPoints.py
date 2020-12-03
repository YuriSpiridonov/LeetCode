"""
    Given n points on a 2D plane where points[i] = [xi, yi], Return the 
    widest vertical area between two points such that no points are inside 
    the area.

    A vertical area is an area of fixed-width extending infinitely along the 
    y-axis (i.e., infinite height). The widest vertical area is the one with 
    the maximum width.

    Note that points on the edge of a vertical area are not considered 
    included in the area.

    Example:
    Input: points = [[8,7],[9,9],[7,4],[9,7]]
    Output: 1
    Explanation: Both the red and the blue area are optimal.

    Example:
    Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    Output: 3

    Constraints:
        - n == points.length
        - 2 <= n <= 10^5
        - points[i].length == 2
        - 0 <= xi, yi <= 10^9
"""
#Difficulty: Medium
#54 / 54 test cases passed.
#Runtime: 852 ms
#Memory Usage: 55 MB

#Runtime: 852 ms, faster than 63.30% of Python3 online submissions for Widest Vertical Area Between Two Points Containing No Points.
#Memory Usage: 55 MB, less than 18.89% of Python3 online submissions for Widest Vertical Area Between Two Points Containing No Points.

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        array = set()
        width = 0
        for x, y in points:
            array.add(x)
        array = list(array)
        array.sort()
        left = array[0]
        for right in array[1:]:
            width = max(width, right-left)
            left = right
        return width
