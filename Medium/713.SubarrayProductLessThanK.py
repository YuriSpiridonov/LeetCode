"""
    Your are given an array of positive integers nums.

    Count and print the number of (contiguous) subarrays where the product of 
    all the elements in the subarray is less than k.

    Example:
    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are: 
                 [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
                 Note that [10, 5, 2] is not included as the product of 100 is 
                 not strictly less than k.

    Note:
        - 0 < nums.length <= 50000.
        - 0 < nums[i] < 1000.
        - 0 <= k < 10^6.
"""
#Difficulty: Medium
#84 / 84 test cases passed.
#Runtime: 1048 ms
#Memory Usage: 18.4 MB

#Runtime: 1048 ms, faster than 100.00% of Python3 online submissions for Subarray Product Less Than K.
#Memory Usage: 18.4 MB, less than 5.02% of Python3 online submissions for Subarray Product Less Than K.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        prod = 1
        count = 0
        length = len(nums)
        for j in range(length):    
            prod *= nums[j]
            while i < j and prod >= k:
                prod //= nums[i]
                i += 1
            if prod < k:
                count += j - i + 1
        return count
