"""
    Given an array nums. We define a running sum of an array as 
    runningSum[i] = sum(nums[0]…nums[i]).
    
    Return the running sum of nums.
    
    Example:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
    
    Constraints:
        - 1 <= nums.length <= 1000
        - -10^6 <= nums[i] <= 10^6
"""
#Difficulty: Easy
#53 / 53 test cases passed.
#Runtime: 36 ms
#Memory Usage: 13.9 MB

#Runtime: 36 ms, faster than 92.99% of Python3 online submissions for Running Sum of 1d Array.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Running Sum of 1d Array.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
