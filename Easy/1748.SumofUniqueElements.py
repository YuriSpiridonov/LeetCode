'''
    You are given an integer array nums. The unique elements 
    of an array are the elements that appear exactly once in 
    the array.

    Return the sum of all the unique elements of nums.

    Example:
    Input: nums = [1,2,3,2]
    Output: 4
    Explanation: The unique elements are [1,3], and the sum 
                 is 4.

    Example:
    Input: nums = [1,1,1,1,1]
    Output: 0
    Explanation: There are no unique elements, and the sum 
                 is 0.

    Example:
    Input: nums = [1,2,3,4,5]
    Output: 15
    Explanation: The unique elements are [1,2,3,4,5], and 
                 the sum is 15.

    Constraints:
        - 1 <= nums.length <= 100
        - 1 <= nums[i] <= 100
'''
#Difficulty: Easy
#73 / 73 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.4 MB

#Runtime: 28 ms, faster than 96.38% of Python3 online submissions for Sum of Unique Elements.
#Memory Usage: 14.4 MB, less than 15.39% of Python3 online submissions for Sum of Unique Elements.

from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(num for num, count in Counter(nums).items() if count == 1)