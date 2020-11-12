"""
    Given a collection of numbers, nums, that might contain duplicates, 
    return all possible unique permutations in any order.

    Example:
    Input: nums = [1,1,2]
    Output:
    [[1,1,2],
     [1,2,1],
     [2,1,1]]

    Example:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Constraints:
        - 1 <= nums.length <= 8
        - -10 <= nums[i] <= 10
"""
#Difficulty: Medium
#33 / 33 test cases passed.
#Runtime: 60 ms
#Memory Usage: 14.3 MB

#Runtime: 60 ms, faster than 51.59% of Python3 online submissions for Permutations II.
#Memory Usage: 14.3 MB, less than 10.37% of Python3 online submissions for Permutations II.

import itertools

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(itertools.permutations(nums))
