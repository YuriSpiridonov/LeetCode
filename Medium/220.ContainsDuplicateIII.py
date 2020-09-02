"""
    Given an array of integers, find out whether there are two distinct indices 
    i and j in the array such that the absolute difference between nums[i] and 
    nums[j] is at most t and the absolute difference between i and j is at most 
    k.

    Example:
    Input: nums = [1,2,3,1], k = 3, t = 0
    Output: true

    Example:
    Input: nums = [1,0,1,1], k = 1, t = 2
    Output: true

    Example:
    Input: nums = [1,5,9,1,5,9], k = 2, t = 3
    Output: false
"""
#Difficulty: Medium
#41 / 41 test cases passed.
#Runtime: 52 ms
#Memory Usage: 17.8 MB

#Runtime: 52 ms, faster than 96.30% of Python3 online submissions for Contains Duplicate III.
#Memory Usage: 17.8 MB, less than 9.93% of Python3 online submissions for Contains Duplicate III.

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        i = 0
        l = len(nums)
        j = min(i + k + 1, l)
        if l > 1 and k != 0 and not (t == 0 and l == len(set(nums))):
            while i <= l:
                temp = nums[i:j]
                x = 0
                y = len(temp) - 1
                while x < y:
                    if abs(temp[x] - temp[y]) <= t:
                        return True
                    if temp[x] > temp[y]:
                        x += 1
                    else:
                        y -= 1
                i += 1
                j = min(i + k + 1, l)
        return False
