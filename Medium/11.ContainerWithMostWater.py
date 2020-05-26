"""
    Given n non-negative integers a1, a2, ..., an , where each represents 
    a point at coordinate (i, ai). n vertical lines are drawn such that 
    the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
    which together with x-axis forms a container, such that the container 
    contains the most water.
    Note: You may not slant the container and n is at least 2.
    
    Example:
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49
"""
#Difficulty: Medium
#50 / 50 test cases passed.
#Runtime: 128 ms
#Memory Usage: 15.2 MB

#Runtime: 128 ms, faster than 79.12% of Python3 online submissions for Container With Most Water.
#Memory Usage: 15.2 MB, less than 5.26% of Python3 online submissions for Container With Most Water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        most_water = 0
        while i <= j:
            most_water = max(most_water, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return most_water
