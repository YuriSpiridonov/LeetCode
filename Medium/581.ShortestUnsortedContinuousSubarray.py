'''
    Given an integer array nums, you need to find one 
    continuous subarray that if you only sort this subarray 
    in ascending order, then the whole array will be sorted 
    in ascending order.

    Return the shortest such subarray and output its length.

    Example:
    Input: nums = [2,6,4,8,10,9,15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in 
                 ascending order to make the whole array 
                 sorted in ascending order.

    Example:
    Input: nums = [1,2,3,4]
    Output: 0

    Example:
    Input: nums = [1]
    Output: 0

    Constraints:
        - 1 <= nums.length <= 10^4
        - -10^5 <= nums[i] <= 10^5

    Follow up: Can you solve it in O(n) time complexity?
'''
#Difficulty: Medium
#307 / 307 test cases passed.
#Runtime: 204 ms
#Memory Usage: 15.5 MB

#Runtime: 204 ms, faster than 68.88% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
#Memory Usage: 15.5 MB, less than 34.34% of Python3 online submissions for Shortest Unsorted Continuous Subarray.

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        array = sorted(nums)
        indices = []
        for i in range(len(nums)):
            if nums[i] != array[i]:
                indices.append(i)
        return 1 + indices[-1] - indices[0] if indices else 0