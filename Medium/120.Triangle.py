"""
    Given a triangle, find the minimum path sum from top to bottom. Each step 
    you may move to adjacent numbers on the row below.

    For example, given the following triangle
        [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

    Note:
        Bonus point if you are able to do this using only O(n) extra space, 
        where n is the total number of rows in the triangle.
"""
#Difficulty: Medium
#43 / 43 test cases passed.
#Runtime: 64 ms
#Memory Usage: 14.2 MB

#Runtime: 64 ms, faster than 69.24% of Python3 online submissions for Triangle.
#Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Triangle.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        path = triangle.pop(0)
        while triangle:
            level = triangle.pop(0)
            for i in range(len(level)):
                if i-1 >= 0 and i+1 <= len(path):
                    level[i] += min(path[i-1], path[i])
                elif i-1 < 0:
                    level[i] += path[i]
                elif i+1 >= len(path):
                    level[i] += path[i-1]
            path = level
        return min(path) 
