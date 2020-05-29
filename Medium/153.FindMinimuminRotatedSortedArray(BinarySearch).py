"""
    Suppose an array sorted in ascending order is rotated at some pivot unknown 
    to you beforehand.
    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
    Find the minimum element.
    
    You may assume no duplicate exists in the array.
    
    Example:
    Input: [3,4,5,1,2] 
    Output: 1
"""
#Difficulty: Medium
#146 / 146 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14 MB

#Runtime: 36 ms, faster than 88.91% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
#Memory Usage: 14 MB, less than 6.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
    
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]
            if nums[m] < nums[l]:
                r = m
            else:
                l = m + 1 
