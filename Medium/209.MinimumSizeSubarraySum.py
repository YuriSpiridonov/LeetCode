"""
    Given an array of n positive integers and a positive integer s, find the 
    minimal length of a contiguous subarray of which the sum ≥ s. 
    If there isn't one, return 0 instead.
    
    Example: 
    Input: s = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: the subarray [4,3] has the minimal length under the problem 
    constraint.
    
    Follow up:
    If you have figured out the O(n) solution, try coding another solution of 
    which the time complexity is O(n log n). 
"""
#Difficulty: Medium
#15 / 15 test cases passed.
#Runtime: 72 ms
#Memory Usage: 16.2 MB

#Runtime: 72 ms, faster than 87.67% of Python3 online submissions for Minimum Size Subarray Sum.
#Memory Usage: 16.2 MB, less than 7.69% of Python3 online submissions for Minimum Size Subarray Sum.

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or sum(nums) < s: return 0
        if s in nums or s < max(nums): return 1
        i = 0
        l = length = len(nums)
        summ = 0
        for j in range(length):
            summ += nums[j]
            while summ >= s and i <= j:
                l = min(l, 1 + j - i)
                summ -= nums[i]
                i += 1
        return l
