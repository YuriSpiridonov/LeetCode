'''
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as 
nums such that result[i] is equal to the summation of absolute 
differences between nums[i] and all the other elements in the 
array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) 
where 0 <= j < nums.length and j != i (0-indexed).

Example:
Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
             result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
             result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
             result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.

Example:
Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]

Constraints:
    - 2 <= nums.length <= 10^5
    - 1 <= nums[i] <= nums[i + 1] <= 10^4
'''
#Difficulty:Medium
#59 / 59 test cases passed.
#Runtime: 956 ms
#Memory Usage: 29.7 MB

#Runtime: 956 ms, faster than 25.00% of Python3 online submissions for Sum of Absolute Differences in a Sorted Array.
#Memory Usage: 29.7 MB, less than 50.00% of Python3 online submissions for Sum of Absolute Differences in a Sorted Array.

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        length = len(nums)
        result = []
        for index, num in enumerate(nums):
            right -= num
            value = abs(num*index - left) + abs(num*(length-index-1) - right)
            result.append(value)
            left += num
        return result
