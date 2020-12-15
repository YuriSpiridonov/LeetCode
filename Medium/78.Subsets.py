'''
    Given an integer array nums, return all possible subsets 
    (the power set).

    The solution set must not contain duplicate subsets.

    Example:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    Example:
    Input: nums = [0]
    Output: [[],[0]]

    Constraints:
        - 1 <= nums.length <= 10
        - -10 <= nums[i] <= 10
'''
#Difficulty: Medium
#10 / 10 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.2 MB

#Runtime: 28 ms, faster than 93.50% of Python3 online submissions for Subsets.
#Memory Usage: 14.2 MB, less than 75.87% of Python3 online submissions for Subsets.

from itertools import combinations 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(1, 1+len(nums)):
            result += combinations(nums, i)
        return result
