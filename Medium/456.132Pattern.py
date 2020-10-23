"""
    Given an array of n integers nums, a 132 pattern is a subsequence of three 
    integers nums[i], nums[j] and nums[k] such that i < j < k and 
    nums[i] < nums[k] < nums[j].
    Return true if there is a 132 pattern in nums, otherwise, return false.

    Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or 
               the O(n) solution?

    Example:
    Input: nums = [1,2,3,4]
    Output: false
    Explanation: There is no 132 pattern in the sequence.

    Example:
    Input: nums = [3,1,4,2]
    Output: true
    Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

    Example:
    Input: nums = [-1,3,2,0]
    Output: true
    Explanation: There are three 132 patterns in the sequence: 
                 [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

    Constraints:
        - n == nums.length
        - 1 <= n <= 10**4
        - -10**9 <= nums[i] <= 10**9
"""
#Difficulty: Medium
#96 / 96 test cases passed.
#Runtime: 8872 ms
#Memory Usage: 15.2 MB

#Runtime: 8872 ms, faster than 5.05% of Python3 online submissions for 132 Pattern.
#Memory Usage: 15.2 MB, less than 44.22% of Python3 online submissions for 132 Pattern.

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        nums_i = float(inf)
        length = len(nums)
        for j in range(length):
            nums_i = min(nums_i, nums[j])
            for k in range(j+1, length):
                if nums_i < nums[k] < nums[j]:
                    return True
        return False
