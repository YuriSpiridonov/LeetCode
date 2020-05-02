"""
Given an array of integers, return indices of the two numbers such that they 
add up to a specific target.
You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
#Difficulty: Easy
#29 / 29 test cases passed.
#Runtime: 1172 ms
#Memory Usage: 14.7 MB

#Runtime: 1152 ms, faster than 27.16% of Python3 online submissions for Two Sum.
#Memory Usage: 14.6 MB, less than 18.14% of Python3 online submissions for Two Sum.
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        l = len(nums)
        for i in range(l):
            n = nums[i]
            d = target - n
            if d in nums[i+1:]:
                return [nums.index(n), i + nums[i+1:].index(d) + 1]
