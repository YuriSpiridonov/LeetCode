'''
    Given an array of integers nums, sort the array in 
    ascending order.

    Example:
    Input: nums = [5,2,3,1]
    Output: [1,2,3,5]

    Example:
    Input: nums = [5,1,1,2,0,0]
    Output: [0,0,1,1,2,5]

    Constraints:
        - 1 <= nums.length <= 50000
        - -50000 <= nums[i] <= 50000
'''
#Difficulty: Medium
#11 / 11 test cases passed.
#Runtime: 124 ms
#Memory Usage: 20.4 MB

#Runtime: 124 ms, faster than 97.55% of Python3 online submissions for Sort an Array.
#Memory Usage: 20.4 MB, less than 54.14% of Python3 online submissions for Sort an Array.

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
