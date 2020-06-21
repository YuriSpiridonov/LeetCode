"""
    Given an array with n objects colored red, white or blue, sort them in-place 
    so that objects of the same color are adjacent, with the colors in the order 
    red, white and blue.
    Here, we will use the integers 0, 1, and 2 to represent the color red, white, 
    and blue respectively.
    
    Note: You are not suppose to use the library's sort function for this problem.
    
    Example:
    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    
    Follow up:
    - A rather straight forward solution is a two-pass algorithm using counting 
      sort.
    - First, iterate the array counting number of 0's, 1's, and 2's, then 
      overwrite array with total number of 0's, then 1's and followed by 2's.
    - Could you come up with a one-pass algorithm using only constant space?
"""
#Difficulty: Medium
#Algorithm: Quick Sort
#87 / 87 test cases passed.
#Runtime: 24 ms
#Memory Usage: 13.7 MB
            
#Runtime: 24 ms, faster than 98.28% of Python3 online submissions for Sort Colors.
#Memory Usage: 13.7 MB, less than 84.16% of Python3 online submissions for Sort Colors.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = 0
        hi = len(nums) - 1
        self.quickSort(nums, lo, hi)
    
    def quickSort(self, nums, lo, hi):
        if lo <= hi:
            p = self.partition(nums, lo, hi)
            self.quickSort(nums, lo, p-1)
            self.quickSort(nums, p+1, hi)

    def partition(self, nums, lo, hi):
        i = lo - 1
        pivot = nums[hi]
        for j in range(lo, hi):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[hi] = nums[hi], nums[i+1]
        return i+1
