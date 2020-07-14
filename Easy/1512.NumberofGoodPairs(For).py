"""
    Given an array of integers nums.
    A pair (i,j) is called good if nums[i] == nums[j] and i < j.
    Return the number of good pairs.

    Example:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

    Constraints:
        - 1 <= nums.length <= 100
        - 1 <= nums[i] <= 100
"""
#Difficulty: Easy
#48 / 48 test cases passed.
#Runtime: 60 ms
#Memory Usage: 13.9 MB   

#Runtime: 60 ms, faster than 33.33% of Python3 online submissions for Number of Good Pairs.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.    

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] == nums[j]:
                    count += 1
        return count
