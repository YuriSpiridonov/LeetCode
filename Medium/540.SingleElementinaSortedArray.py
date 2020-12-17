'''
    You are given a sorted array consisting of only integers 
    where every element appears exactly twice, except for one 
    element which appears exactly once. Find this single 
    element that appears only once.

    Follow up: Your solution should run in O(log n) time 
    and O(1) space.

    Example:
    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2

    Example:
    Input: nums = [3,3,7,7,10,11,11]
    Output: 10

    Constraints:
        - 1 <= nums.length <= 10^5
        - 0 <= nums[i] <= 10^5
'''
#Difficulty: Medium
#14 / 14 test cases passed.
#Runtime: 72 ms
#Memory Usage: 16.3 MB

#Runtime: 72 ms, faster than 42.45% of Python3 online submissions for Single Element in a Sorted Array.
#Memory Usage: 16.3 MB, less than 39.99% of Python3 online submissions for Single Element in a Sorted Array.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left+right) // 2
            if nums[middle] == nums[middle+1]: 
                if not middle % 2 and (middle+1) % 2:
                    left = middle + 1
                else:
                    right = middle
            elif nums[middle] == nums[middle-1]:
                if middle % 2 and not (middle-1) % 2:
                    left = middle + 1
                else:
                    right = middle
            else:
                return nums[middle]
        return nums[right]
