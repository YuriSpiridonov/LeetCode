'''
    Given an unsorted array of integers nums, return the 
    length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

    Example:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence 
                 is [1, 2, 3, 4]. Therefore its length is 4.

    Example:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

    Constraints:
        - 0 <= nums.length <= 10^5
        - -10^9 <= nums[i] <= 10^9
'''
#Difficulty: Medium
#70 / 70 test cases passed.
#Runtime: 216 ms
#Memory Usage: 25.9 MB

#Runtime: 216 ms, faster than 30.78% of Python3 online submissions for Longest Consecutive Sequence.
#Memory Usage: 25.9 MB, less than 15.32% of Python3 online submissions for Longest Consecutive Sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        length = 0
        prev = nums[0]
        sub_length = 1

        for num in nums[1:]:
            if num-1 == prev:
                sub_length += 1
            else:
                length = max(length, sub_length)
                sub_length = 1
            prev = num
        return max(length, sub_length)
