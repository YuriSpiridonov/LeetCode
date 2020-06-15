"""
    Suppose an array sorted in ascending order is rotated at some pivot unknown 
    to you beforehand.
    (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
    You are given a target value to search. If found in the array return true, 
    otherwise return false.
    
    Example:
    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true
    
    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false
    
    Follow up:
        - This is a follow up problem to Search in Rotated Sorted Array, where 
          nums ay contain duplicates.
        - Would this affect the run-time complexity? How and why?
"""
#Difficulty: Medium
#275 / 275 test cases passed.
#Runtime: 52 ms
#Memory Usage: 14.2 MB

#Runtime: 52 ms, faster than 77.59% of Python3 online submissions for Search in Rotated Sorted Array II.
#Memory Usage: 14.2 MB, less than 5.72% of Python3 online submissions for Search in Rotated Sorted Array II.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False
