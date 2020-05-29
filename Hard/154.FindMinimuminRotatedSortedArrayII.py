"""
    Suppose an array sorted in ascending order is rotated at some pivot unknown 
    to you beforehand.
    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
    Find the minimum element.
    The array may contain duplicates.
    
    Example:
    Input: [2,2,2,0,1]
    Output: 0
    
    Note:
    - This is a follow up problem to Find Minimum in Rotated Sorted Array.
    - Would allow duplicates affect the run-time complexity? How and why?
"""
#Difficulty: Hard
#192 / 192 test cases passed.
#Runtime: 48 ms
#Memory Usage: 14.3 MB

#Runtime: 48 ms, faster than 92.02% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
#Memory Usage: 14.3 MB, less than 5.88% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[0]:
                return nums[i]
        return nums[0] 
