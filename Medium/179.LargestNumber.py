"""
    Given a list of non negative integers, arrange them such that they form the 
    largest number.

    Example:
    Input: [10,2]
    Output: "210"

    Example:
    Input: [3,30,34,5,9]
    Output: "9534330"

    Note: The result may be very large, so you need to return a string instead 
          of an integer.
"""
#Difficulty: Medium
#222 / 222 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14.1 MB

#Runtime: 40 ms, faster than 69.37% of Python3 online submissions for Largest Number.
#Memory Usage: 14.1 MB, less than 7.82% of Python3 online submissions for Largest Number.

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        length = len(nums)
        nums = sorted([str(nums[i]) for i in range(length)], reverse=True)
        for j in range(1, length):
            for i in range(length-j):
                if nums[i+1] in nums[i] and nums[i+1] != nums[i]:
                    if nums[i+1] + nums[i] > nums[i] + nums[i+1]:
                        nums[i+1], nums[i] = nums[i], nums[i+1]
        return ''.join(nums) if nums[0] != '0' else '0'
