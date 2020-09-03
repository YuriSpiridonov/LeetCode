"""
    Given a collection of distinct integers, return all possible permutations.

    Example:
    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
"""
#Difficulty: Medium
#25 / 25 test cases passed.
#Runtime: 32 ms
#Memory Usage: 13.7 MB

#Runtime: 32 ms, faster than 97.95% of Python3 online submissions for Permutations.
#Memory Usage: 13.7 MB, less than 97.13% of Python3 online submissions for Permutations.

import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums)
