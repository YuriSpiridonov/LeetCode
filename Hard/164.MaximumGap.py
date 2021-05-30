'''
    Given an integer array nums, return the maximum difference 
    between two successive elements in its sorted form. If 
    the array contains less than two elements, return 0.

    You must write an algorithm that runs in linear time and 
    uses linear extra space.

    Example:
    Input: nums = [3,6,9,1]
    Output: 3
    Explanation: The sorted form of the array is [1,3,6,9], 
                 either (3,6) or (6,9) has the maximum 
                 difference 3.

    Example:
    Input: nums = [10]
    Output: 0
    Explanation: The array contains less than 2 elements, 
                 therefore return 0.

    Constraints:
        - 1 <= nums.length <= 10^4
        - 0 <= nums[i] <= 10^9
'''
#Difficulty: Hard
#17 / 17 test cases passed.
#Runtime: 56 ms
#Memory Usage: 14.9 MB

#Runtime: 56 ms, faster than 61.19% of Python3 online submissions for Maximum Gap.
#Memory Usage: 14.9 MB, less than 99.25% of Python3 online submissions for Maximum Gap.

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        difference = 0
        for i in range(1,len(nums)):
            difference = max(difference, abs(nums[i]-nums[i-1]))
        return difference
