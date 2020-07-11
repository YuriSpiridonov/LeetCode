"""
    Given an array of integers and an integer k, find out whether there are two 
    distinct indices i and j in the array such that nums[i] = nums[j] and the 
    absolute difference between i and j is at most k.

    Example:
    Input: nums = [1,2,3,1], k = 3
    Output: true
"""
#Difficulty: Easy
#23 / 23 test cases passed.
#Runtime: 92 ms
#Memory Usage: 24.8 MB

#Runtime: 92 ms, faster than 86.57% of Python3 online submissions for Contains Duplicate II.
#Memory Usage: 24.8 MB, less than 11.60% of Python3 online submissions for Contains Duplicate II.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                if i - d[num][-1] <= k:
                    return True
                d[num].append(i)
            else:
                d[num] = [i]
        return False
