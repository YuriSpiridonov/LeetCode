'''
    We define a harmonious array as an array where the 
    difference between its maximum value and its minimum 
    value is exactly 1.

    Given an integer array nums, return the length of its 
    longest harmonious subsequence among all its possible 
    subsequences.

    A subsequence of array is a sequence that can be derived 
    from the array by deleting some or no elements without 
    changing the order of the remaining elements.

    Example:
    Input: nums = [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is 
                 [3,2,2,2,3].

    Example:
    Input: nums = [1,2,3,4]
    Output: 2

    Example:
    Input: nums = [1,1,1,1]
    Output: 0

    Constraints:
        - 1 <= nums.length <= 2 * 10^4
        - -10^9 <= nums[i] <= 10^9
'''
#Difficulty: Easy
#206 / 206 test cases passed.
#Runtime: 424 ms
#Memory Usage: 16 MB

#Runtime: 424 ms, faster than 13.69% of Python3 online submissions for Longest Harmonious Subsequence.
#Memory Usage: 16 MB, less than 39.46% of Python3 online submissions for Longest Harmonious Subsequence.

from collections import defaultdict

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        numbers = defaultdict(int)
        result = 0
        for num in nums:
            numbers[num] += 1
        for num in numbers.keys():
            if num+1 in numbers.keys():
                result = max(result, numbers[num] + numbers[num+1])
        return result