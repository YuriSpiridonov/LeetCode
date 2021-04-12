'''
    Given an array of positive integers nums, return the 
    maximum possible sum of an ascending subarray in nums.

    A subarray is defined as a contiguous sequence of numbers 
    in an array.

    A subarray [numsl, numsl+1, ..., numsr-1, numsr] is 
    ascending if for all i where l <= i < r, numsi < numsi+1. 
    Note that a subarray of size 1 is ascending.

    Example:
    Input: nums = [10,20,30,5,10,50]
    Output: 65
    Explanation: [5,10,50] is the ascending subarray with 
                 the maximum sum of 65.

    Example:
    Input: nums = [10,20,30,40,50]
    Output: 150
    Explanation: [10,20,30,40,50] is the ascending subarray 
                 with the maximum sum of 150.

    Example:
    Input: nums = [12,17,15,13,10,11,12]
    Output: 33
    Explanation: [10,11,12] is the ascending subarray with 
                 the maximum sum of 33.

    Example:
    Input: nums = [100,10,1]
    Output: 100

    Constraints:
        - 1 <= nums.length <= 100
        - 1 <= nums[i] <= 100
'''
#Difficulty: Easy
#104 / 104 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14 MB

#Runtime: 36 ms, faster than 63.67% of Python3 online submissions for Maximum Ascending Subarray Sum.
#Memory Usage: 14 MB, less than 91.31% of Python3 online submissions for Maximum Ascending Subarray Sum.

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i = 0
        j = i + 1
        nums.append(0)
        length = len(nums)
        result = 0
        while j < length:
            if nums[j-1] < nums[j]:
                j += 1
            else:
                result = max(result, sum(nums[i:j]))
                i = j
                j = i + 1
        return result