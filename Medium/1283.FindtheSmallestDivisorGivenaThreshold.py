"""
    Given an array of integers nums and an integer threshold, we will choose 
    a positive integer divisor and divide all the array by it and sum the 
    result of the division. Find the smallest divisor such that the result 
    mentioned above is less than or equal to threshold.

    Each result of division is rounded to the nearest integer greater than or 
    equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

    It is guaranteed that there will be an answer.

    Example:
    Input: nums = [1,2,5,9], threshold = 6
    Output: 5
    Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
                 If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if 
                 the divisor is 5 the sum will be 5 (1+1+1+2). 

    Example:
    Input: nums = [2,3,5,7,11], threshold = 11
    Output: 3

    Example:
    Input: nums = [19], threshold = 5
    Output: 4

    Constraints:
        - 1 <= nums.length <= 5 * 10^4
        - 1 <= nums[i] <= 10^6
        - nums.length <= threshold <= 10^6
"""
#Difficulty: Medium
#61 / 61 test cases passed.
#Runtime: 364 ms
#Memory Usage: 20 MB

#Runtime: 364 ms, faster than 88.71% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.
#Memory Usage: 20 MB, less than 79.06% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        while l < r:
            m = (l+r) // 2
            result = sum([1 + n//m if n%m else n//m for n in nums])
            if result > threshold:
                l = m + 1
            else:
                r = m
        return l
