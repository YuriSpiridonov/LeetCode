"""
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
    find the one that is missing from the array.
    
    Example:
    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8
    
    Note:
    Your algorithm should run in linear runtime complexity. Could you implement 
    it using only constant extra space complexity?
"""
#Difficulty: Easy
#122 / 122 test cases passed.
#Runtime: 132 ms
#Memory Usage: 14.9 MB

#Runtime: 132 ms, faster than 93.14% of Python3 online submissions for Missing Number.
#Memory Usage: 14.9 MB, less than 89.02% of Python3 online submissions for Missing Number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_number = max(nums) + 1
        range_sum = sum([i for i in range(max_number)])
        nums_sum = sum(nums)
        missing_number = range_sum - nums_sum
        return missing_number if missing_number not in nums else max_number
