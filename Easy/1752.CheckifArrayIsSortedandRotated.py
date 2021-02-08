'''
    Given an array nums, return true if the array was 
    originally sorted in non-decreasing order, then rotated 
    some number of positions (including zero). Otherwise, 
    return false.

    There may be duplicates in the original array.

    Note: An array A rotated by x positions results in an 
    array B of the same length such that 
    A[i] == B[(i+x) % A.length], where % is the modulo 
    operation.

    Example:
    Input: nums = [3,4,5,1,2]
    Output: true
    Explanation: [1,2,3,4,5] is the original sorted array.
                 You can rotate the array by x = 3 positions 
                 to begin on the the element of value 3: 
                 [3,4,5,1,2].

    Example:
    Input: nums = [2,1,3,4]
    Output: false
    Explanation: There is no sorted array once rotated that 
                 can make nums.

    Example:
    Input: nums = [1,2,3]
    Output: true
    Explanation: [1,2,3] is the original sorted array.
                 You can rotate the array by x = 0 positions 
                 (i.e. no rotation) to make nums.

    Example:
    Input: nums = [1,1,1]
    Output: true
    Explanation: [1,1,1] is the original sorted array.
    You can rotate any number of positions to make nums.

    Example:
    Input: nums = [2,1]
    Output: true
    Explanation: [1,2] is the original sorted array.
                 You can rotate the array by x = 5 positions 
                 to begin on the element of value 2: [2,1].

    Constraints:
        - 1 <= nums.length <= 100
        - 1 <= nums[i] <= 100
'''
#Difficulty: Easy
#96 / 96 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.3 MB

#Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Check if Array Is Sorted and Rotated.
#Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Check if Array Is Sorted and Rotated.

class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return nums[-1] <= nums[0] and nums[i:] == sorted(nums[i:])
        return True