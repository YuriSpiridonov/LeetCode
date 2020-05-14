"""
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as 
    one sorted array.
    
    Note:
    The number of elements initialized in nums1 and nums2 are m and n 
    respectively.
    You may assume that nums1 has enough space 
    (size that is greater or equal to m + n) 
    to hold additional elements from nums2.
    
    Example:
    Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3
    Output: [1,2,2,3,5,6]
"""
#Difficulty: Easy
#59 / 59 test cases passed.
#Runtime: 32 ms
#Memory Usage: 13.8 MB

#Runtime: 32 ms, faster than 88.10% of Python3 online submissions for Merge Sorted Array.
#Memory Usage: 13.8 MB, less than 6.15% of Python3 online submissions for Merge Sorted Array.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = len(nums1)
        s = m + n
        if s <= l:
            for num2 in nums2:
                s -= 1
                nums1[s] = num2
            nums1.sort()

#Difficulty: Easy
#59 / 59 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.1 MB

#Runtime: 28 ms, faster than 97.31% of Python3 online submissions for Merge Sorted Array.
#Memory Usage: 14.1 MB, less than 6.15% of Python3 online submissions for Merge Sorted Array.
            
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()   
