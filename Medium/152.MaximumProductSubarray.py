"""
    Given an integer array nums, find the contiguous subarray within an array 
    (containing at least one number) which has the largest product.

    Example:
    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

    Example:
    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
#Difficulty: Medium
#187 / 187 test cases passed.
#Runtime: 56 ms
#Memory Usage: 14 MB

#Runtime: 56 ms, faster than 78.26% of Python3 online submissions for Maximum Product Subarray.
#Memory Usage: 14 MB, less than 59.43% of Python3 online submissions for Maximum Product Subarray.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum_product = maximum = minimum = nums[0]
        for i in range(1, len(nums)):
            local_maximum = nums[i] * maximum
            local_minimum = nums[i] * minimum
            maximum = max(nums[i], max(local_maximum, local_minimum))
            minimum = min(nums[i], min(local_maximum, local_minimum))
            maximum_product = max(maximum_product, maximum)
        return maximum_product
