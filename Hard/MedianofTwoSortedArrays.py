"""
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).
    You may assume nums1 and nums2 cannot be both empty.
    
    Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    The median is 2.0
    Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    The median is (2 + 3)/2 = 2.5
"""
#Difficulty: Hard
#2085 / 2085 test cases passed.
#Runtime: 96 ms
#Memory Usage: 14 MB

#Runtime: 96 ms, faster than 63.37% of Python3 online submissions for Median of Two Sorted Arrays.
#Memory Usage: 14 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.

class Solution:
    #def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(nums1, nums2):
        nums = sorted(nums1+nums2)
        med = 0
        if len(nums)%2 == 0:
            med = (nums[(len(nums)//2)-1]+nums[len(nums)//2])/2
        else:
            med = nums[len(nums)//2]
        return med
        
#Tests
nums1 = [1, 2]
nums2 = [3, 4]
print(Solution.findMedianSortedArrays(nums1, nums2),'2,5')
