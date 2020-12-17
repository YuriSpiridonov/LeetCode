'''
    You are given an integer array nums and an integer k.

    In one operation, you can pick two numbers from the array 
    whose sum equals k and remove them from the array.

    Return the maximum number of operations you can perform 
    on the array.

    Example:
    Input: nums = [1,2,3,4], k = 5
    Output: 2
    Explanation: Starting with nums = [1,2,3,4]:
                 - Remove numbers 1 and 4, then nums = [2,3]
                 - Remove numbers 2 and 3, then nums = []
                 There are no more pairs that sum up to 5, 
                 hence a total of 2 operations.

    Example:
    Input: nums = [3,1,3,4,3], k = 6
    Output: 1
    Explanation: Starting with nums = [3,1,3,4,3]:
                 - Remove the first two 3's, then nums = [1,4,3]
                 There are no more pairs that sum up to 6, 
                 hence a total of 1 operation.

    Constraints:
        - 1 <= nums.length <= 10^5
        - 1 <= nums[i] <= 10^9
        - 1 <= k <= 10^9
'''
#Difficulty: Medium
#51 / 51 test cases passed.
#Runtime: 620 ms
#Memory Usage: 27.4 MB

#Runtime: 620 ms, faster than 97.79% of Python3 online submissions for Max Number of K-Sum Pairs.
#Memory Usage: 27.4 MB, less than 41.54% of Python3 online submissions for Max Number of K-Sum Pairs.

from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = 0
        numbers = Counter(nums)
        for x in numbers.keys():
            if x == k-x:
                pairs += numbers[x]
            elif k-x in numbers:
                pairs += min(numbers[x], numbers[k-x])
        return pairs//2
