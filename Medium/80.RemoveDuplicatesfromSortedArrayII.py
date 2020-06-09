"""
    Given a sorted array nums, remove the duplicates in-place such that 
    duplicates appeared at most twice and return the new length.
    Do not allocate extra space for another array, you must do this by 
    modifying the input array in-place with O(1) extra memory.
    
    Example:
    Given nums = [0,0,1,1,1,1,2,3,3],
    Your function should return length = 7, with the first seven elements of 
    nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
    It doesn't matter what values are set beyond the returned length.
    
    Clarification:
    Confused why the returned value is an integer but your answer is an array?
    Note that the input array is passed in by reference, which means 
    modification to the input array will be known to the caller as well.
"""
#Difficulty: Medium
#166 / 166 test cases passed.
#Runtime: 76 ms
#Memory Usage: 14.1 MB

#Runtime: 76 ms, faster than 16.97% of Python3 online submissions for Remove Duplicates from Sorted Array II.
#Memory Usage: 14.1 MB, less than 5.41% of Python3 online submissions for Remove Duplicates from Sorted Array II.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        for num in s:
            index = nums.index(num)
            count = nums.count(num)
            if count >= 2:
                nums[:] = nums[:index] + nums[index:index+2] + nums[index+count:]
