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
#Runtime: 92 ms
#Memory Usage: 15.1 MB

#Runtime: 92 ms, faster than 35.83% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
#Memory Usage: 15.1 MB, less than 5.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums: return [-1, -1]
        i = nums.index(target)
        j = nums[::-1].index(target)
        return [i, len(nums) - j - 1]
    
#Difficulty: Medium
#88 / 88 test cases passed.
#Runtime: 88 ms
#Memory Usage: 15.2 MB

#Runtime: 88 ms, faster than 64.44% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
#Memory Usage: 15.2 MB, less than 5.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums: return [-1, -1]
        return [nums.index(target), len(nums) - nums[::-1].index(target) - 1]
