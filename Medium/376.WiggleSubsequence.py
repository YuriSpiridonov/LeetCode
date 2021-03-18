'''
    Given an integer array nums, return the length of the 
    longest wiggle sequence.

    A wiggle sequence is a sequence where the differences 
    between successive numbers strictly alternate between 
    positive and negative. The first difference (if one 
    exists) may be either positive or negative. A sequence 
    with fewer than two elements is trivially a wiggle 
    sequence.
        - For example, [1, 7, 4, 9, 2, 5] is a wiggle 
          sequence because the differences (6, -3, 5, -7, 3) 
          are alternately positive and negative.
        - In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] 
          are not wiggle sequences, the first because its 
          first two differences are positive and the second 
          because its last difference is zero.

    A subsequence is obtained by deleting some elements 
    (eventually, also zero) from the original sequence, 
    leaving the remaining elements in their original order.

    Example:
    Input: nums = [1,7,4,9,2,5]
    Output: 6
    Explanation: The entire sequence is a wiggle sequence.

    Example:
    Input: nums = [1,17,5,10,13,15,10,5,16,8]
    Output: 7
    Explanation: There are several subsequences that achieve 
                 this length. One is [1,17,10,13,10,16,8].

    Example:
    Input: nums = [1,2,3,4,5,6,7,8,9]
    Output: 2

    Constraints:
        - 1 <= nums.length <= 1000
        - 0 <= nums[i] <= 1000

    Follow up: Could you solve this in O(n) time?
'''
#Difficulty: Medium
#26 / 26 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.3 MB

#Runtime: 32 ms, faster than 83.94% of Python3 online submissions for Wiggle Subsequence.
#Memory Usage: 14.3 MB, less than 73.64% of Python3 online submissions for Wiggle Subsequence.

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        if len(nums) > 1:
            length = len(nums)
            positive = nums[1] - nums[0] > 0
            for i in range(length-1):
                if (nums[i+1] - nums[i] > 0) == positive:
                    length -= 1
                else:
                    positive = (nums[i+1] - nums[i] > 0)
            return 1 + length
        else:
            return 1
