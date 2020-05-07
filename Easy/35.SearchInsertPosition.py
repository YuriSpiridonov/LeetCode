"""
    Given a sorted array and a target value, return the index if the target is 
    found. If not, return the index where it would be if it were inserted in 
    order.
    You may assume no duplicates in the array.
    
    Example:
    Input: [1,3,5,6], 7
    Output: 4
"""
#Difficulty: Easy
#62 / 62 test cases passed.
#Runtime: 44 ms
#Memory Usage: 14.5 MB

#Runtime: 44 ms, faster than 91.93% of Python3 online submissions for Search Insert Position.
#Memory Usage: 14.5 MB, less than 5.97% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if m == r and target > nums[m]:
                return m + 1
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return m
