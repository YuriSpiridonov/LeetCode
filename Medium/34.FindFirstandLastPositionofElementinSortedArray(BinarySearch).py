"""
    Given an array of integers nums sorted in ascending order, find the starting 
    and ending position of a given target value.
    Your algorithm's runtime complexity must be in the order of O(log n).
    If the target is not found in the array, return [-1, -1].
    
    Example:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
"""
#Difficulty: Medium
#88 / 88 test cases passed.
#Runtime: 84 ms
#Memory Usage: 15.3 MB

#Runtime: 84 ms, faster than 86.58% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
#Memory Usage: 15.3 MB, less than 7.83% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        length = len(nums)
        l = 0
        r = length - 1
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] == target:
                l = m - 1
                while l > -1 and nums[l] == target:
                    l -= 1
                r = m + 1
                while r < length and nums[r] == target:
                    r += 1
                return [l+1, r-1]
            if nums[m] < target:
                l = m
            else:
                r = m
        
        '''Сrutches for short arrays'''
        if nums[l] == target and nums[r] == target:
            return [l, r]
        if nums[l] == target:
            return [l, l]
        if nums[r] == target:
            return [r, r]

        return [-1, -1]
