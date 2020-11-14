"""
    Given an array nums with n integers, your task is to check if it could 
    become non-decreasing by modifying at most 1 element.

    We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for 
    every i (0-based) such that (0 <= i <= n - 2).

    Example:
    Input: nums = [4,2,3]
    Output: true
    Explanation: You could modify the first 4 to 1 to get a non-decreasing 
                 array.

    Example:
    Input: nums = [4,2,1]
    Output: false
    Explanation: You can't get a non-decreasing array by modify at most one 
                 element.

    Constraints:
        - 1 <= n <= 10 ^ 4
        - -10 ^ 5 <= nums[i] <= 10 ^ 5
"""
#Difficulty: Easy
#334 / 334 test cases passed.
#Runtime: 1116 ms
#Memory Usage: 15.6 MB

#Runtime: 1116 ms, faster than 5.08% of Python3 online submissions for Non-decreasing Array.
#Memory Usage: 15.6 MB, less than 16.93% of Python3 online submissions for Non-decreasing Array.

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        indices = []
        lo = 0
        hi = 0
        nums.append(float(inf))
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                indices.append((i, nums[i+1]))
                lo += 1
            if nums[i] >= nums[i+1]:
                indices.append((i, nums[i+1]))
                hi += 1
            if lo > 1 and hi > 1:
                break
        for index, value in indices:
            if nums[:index] + [value] + nums[index+1:-1] == sorted(nums[:index] + [value] + nums[index+1:-1]):
                return True
        return False if len(nums[:-1]) > 1 else True
