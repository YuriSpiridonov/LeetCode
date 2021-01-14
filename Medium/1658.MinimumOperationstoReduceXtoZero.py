'''
    You are given an integer array nums and an integer x. 
    In one operation, you can either remove the leftmost or 
    the rightmost element from the array nums and subtract 
    its value from x. Note that this modifies the array for 
    future operations.

    Return the minimum number of operations to reduce x to 
    exactly 0 if it's possible, otherwise, return -1.

    Example:
    Input: nums = [1,1,4,2,3], x = 5
    Output: 2
    Explanation: The optimal solution is to remove the last 
                 two elements to reduce x to zero.

    Example:
    Input: nums = [5,6,7,8,9], x = 4
    Output: -1

    Example:
    Input: nums = [3,2,20,1,1,3], x = 10
    Output: 5
    Explanation: The optimal solution is to remove the last 
                 three elements and the first two elements 
                 (5 operations in total) to reduce x to zero.

    Constraints:
        - 1 <= nums.length <= 10^5
        - 1 <= nums[i] <= 10^4
        - 1 <= x <= 10^9
'''
#Difficulty: Medium
#88 / 88 test cases passed.
#Runtime: 1224 ms
#Memory Usage: 36.3 MB

#Runtime: 1224 ms, faster than 64.15% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
#Memory Usage: 36.3 MB, less than 23.24% of Python3 online submissions for Minimum Operations to Reduce X to Zero.

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        index = -1
        length = len(nums)
        n = 0
        numbers = {}

        for num in nums:
            x -= num
        if x == 0:
            return length

        for i in range(len(nums)):
            n += nums[i]
            if n == -x:
                index = i + 1
            if n not in numbers:
                numbers[n] = i
            if n+x in numbers:
                index = max(index, i - numbers[n+x])

        return length - index if index != -1 else index
