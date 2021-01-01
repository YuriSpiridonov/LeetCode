'''
    Given an array of integers nums, find the maximum length 
    of a subarray where the product of all its elements is 
    positive.

    A subarray of an array is a consecutive sequence of zero 
    or more values taken out of that array.

    Return the maximum length of a subarray with positive 
    product.

    Example:
    Input: nums = [1,-2,-3,4]
    Output: 4
    Explanation: The array nums already has a positive 
                 product of 24.

    Example:
    Input: nums = [0,1,-2,-3,-4]
    Output: 3
    Explanation: The longest subarray with positive product 
                 is [1,-2,-3] which has a product of 6.
                 Notice that we cannot include 0 in the 
                 subarray since that'll make the product 0 
                 which is not positive.

    Example:
    Input: nums = [-1,-2,-3,0,1]
    Output: 2
    Explanation: The longest subarray with positive product 
                 is [-1,-2] or [-2,-3].

    Example:
    Input: nums = [-1,2]
    Output: 1

    Example:
    Input: nums = [1,2,3,5,-6,4,0,10]
    Output: 4

    Constraints:
        - 1 <= nums.length <= 10^5
        - -10^9 <= nums[i] <= 10^9
'''
#Difficulty: Medium
#112 / 112 test cases passed.
#Runtime: 4444 ms
#Memory Usage: 28.1 MB

#Runtime: 4444 ms, faster than 5.22% of Python3 online submissions for Maximum Length of Subarray With Positive Product.
#Memory Usage: 28.1 MB, less than 53.91% of Python3 online submissions for Maximum Length of Subarray With Positive Product.

class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        length = 0
        if 0 in nums:
            array = self.splitArray(nums) 
        else:
            array = [nums]

        for sub in array:
            negative = 0
            sub_len = 0
            first_index = None
            last_index = None
            for val in sub:
                sub_len += 1
                if val < 0:
                    if first_index is None:
                        first_index = sub_len
                    last_index = sub_len
                    negative += 1
                if not negative % 2:
                    length = max(length, sub_len)
                else:
                    length = max(length, sub_len - first_index, sub_len - last_index)
        return length

    def splitArray(self, nums):
        i = 0
        arr = []
        while i <= len(nums):
            if i == len(nums) or nums[i] == 0:
                arr.append(nums[:i])
                nums = nums[i+1:]
                i = 0
                if i != len(nums): 
                    continue
            i += 1
        return arr
