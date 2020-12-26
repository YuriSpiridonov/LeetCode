'''
    You are given an array of positive integers nums and want 
    to erase a subarray containing unique elements. The score 
    you get by erasing the subarray is equal to the sum of its 
    elements.

    Return the maximum score you can get by erasing exactly 
    one subarray.

    An array b is called to be a subarray of a if it forms a 
    contiguous subsequence of a, that is, if it is equal to 
    a[l],a[l+1],...,a[r] for some (l,r).

    Example:
    Input: nums = [4,2,4,5,6]
    Output: 17
    Explanation: The optimal subarray here is [2,4,5,6].

    Example:
    Input: nums = [5,2,1,2,5,2,1,2,5]
    Output: 8
    Explanation: The optimal subarray here is [5,2,1] or 
                 [1,2,5].

    Constraints:
        - 1 <= nums.length <= 10^5
        - 1 <= nums[i] <= 10^4
'''
#Difficulty: Medium
#62 / 62 test cases passed.
#Runtime: 2228 ms
#Memory Usage: 27.4 MB

#Runtime: 2228 ms, faster than 33.33% of Python3 online submissions for Maximum Erasure Value.
#Memory Usage: 27.4 MB, less than 33.33% of Python3 online submissions for Maximum Erasure Value.

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = 0
        score = 0
        indices = {}
        length = len(nums)
        for j in range(length):
            if nums[j] not in indices or indices[nums[j]] < i:
                score = max(score, sum(nums[i:j+1]))
            else:
                i = 1 + indices[nums[j]]
            indices[nums[j]] = j
        return score
