"""
    Find the kth largest element in an unsorted array. Note that it is the kth 
    largest element in the sorted order, not the kth distinct element.

    Example:
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5

    Note:
    You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
#Difficulty: Medium
#32 / 32 test cases passed.
#Runtime: 68 ms
#Memory Usage: 14.7 MB

#Runtime: 68 ms, faster than 69.20% of Python3 online submissions for Kth Largest Element in an Array.
#Memory Usage: 14.7 MB, less than 40.96% of Python3 online submissions for Kth Largest Element in an Array.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
