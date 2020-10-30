"""
    Given an unsorted array of integers nums, return the length of the longest 
    continuous increasing subsequence (i.e. subarray). The subsequence must be 
    strictly increasing.

    A continuous increasing subsequence is defined by two indices l and r 
    (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 
    and for each l <= i < r, nums[i] < nums[i + 1].

    Example:
    Input: nums = [1,3,5,4,7]
    Output: 3
    Explanation: The longest continuous increasing subsequence is [1,3,5] with 
                 length 3.
                 Even though [1,3,5,7] is an increasing subsequence, it is not 
                 continuous as elements 5 and 7 are separated by element 4.

    Example:
    Input: nums = [2,2,2,2,2]
    Output: 1
    Explanation: The longest continuous increasing subsequence is [2] with 
                 length 1. Note that it must be strictly increasing.

    Constraints:
        - 0 <= nums.length <= 10**4
        - -10**9 <= nums[i] <= 10**9
"""
#Difficulty: Easy
#36 / 36 test cases passed.
#Runtime: 68 ms
#Memory Usage: 15.1 MB

#Runtime: 68 ms, faster than 93.55% of Python3 online submissions for Longest Continuous Increasing Subsequence.
#Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Longest Continuous Increasing Subsequence.

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        max_count = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count
