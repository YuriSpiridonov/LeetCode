"""
    Given an unsorted integer array, find the smallest missing positive integer.
    
    Example:
    Input: [1,2,0]
    Output: 3
"""
#Difficulty: Hard
#165 / 165 test cases passed.
#Runtime: 32 ms
#Memory Usage: 13.6 MB

#Runtime: 32 ms, faster than 81.62% of Python3 online submissions for First Missing Positive.
#Memory Usage: 13.6 MB, less than 8.70% of Python3 online submissions for First Missing Positive.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        nums = sorted(nums)
        length = len(nums) -1
        index = 0
        for i, n in enumerate(nums):
            if n >= 0:
                index = i
                break
        d = nums[index]
        if d > 1: return 1
        for i, n in enumerate(nums[index + 1:]):
            if d + 1 == n or d == n:
                d = n
            else: break
        return d + 1 if d + 1 > 0 else 1
