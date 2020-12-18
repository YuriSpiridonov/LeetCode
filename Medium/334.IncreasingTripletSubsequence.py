'''
    Given an integer array nums, return true if there exists 
    a triple of indices (i, j, k) such that i < j < k and 
    nums[i] < nums[j] < nums[k]. If no such indices exists, 
    return false.

    Example:
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.

    Example:
    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.

    Example:
    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because 
                 nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

    Constraints:
        1 <= nums.length <= 10^5
        -2^31 <= nums[i] <= 2^31 - 1
'''
#Difficulty: Medium
#61 / 61 test cases passed.
#Runtime: 4360 ms
#Memory Usage: 14.9 MB

#Runtime: 4360 ms, faster than 5.22% of Python3 online submissions for Increasing Triplet Subsequence.
#Memory Usage: 14.9 MB, less than 23.89% of Python3 online submissions for Increasing Triplet Subsequence.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] < nums[j]:
                    if nums[j+1:] and max(nums[j+1:]) > nums[j]:
                        return True
        return False
