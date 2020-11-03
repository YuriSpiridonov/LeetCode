"""
    Given a non-empty array of integers, every element appears three times 
    except for one, which appears exactly once. Find that single one.

    Note:
    Your algorithm should have a linear runtime complexity. Could you 
    implement it without using extra memory?

    Example:
    Input: [2,2,3,2]
    Output: 3

    Example:
    Input: [0,1,0,1,0,1,99]
    Output: 99
"""
#Difficulty: Medium
#11 / 11 test cases passed.
#Runtime: 1756 ms
#Memory Usage: 15.6 MB

#Runtime: 1756 ms, faster than 5.09% of Python3 online submissions for Single Number II.
#Memory Usage: 15.6 MB, less than 69.25% of Python3 online submissions for Single Number II.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for num in nums_set:
            if nums.count(num) == 1:
                return num
