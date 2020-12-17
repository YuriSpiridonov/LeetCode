"""
Given an array of integers nums and an integer target, return 
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    - 2 <= nums.length <= 10^3
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.
"""
#Difficulty: Easy
#52 / 52 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14.6 MB

#Runtime: 40 ms, faster than 96.53% of Python3 online submissions for Two Sum.
#Memory Usage: 14.6 MB, less than 59.48% of Python3 online submissions for Two Sum.
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if target-n in nums[i+1:]:
                return i, i+1+nums[i+1:].index(target-n)
