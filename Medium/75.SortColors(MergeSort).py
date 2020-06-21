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
#Algorithm: Merge Sort
#87 / 87 test cases passed.
#Runtime: 32 ms
#Memory Usage: 13.8 MB

#Runtime: 32 ms, faster than 77.37% of Python3 online submissions for Sort Colors.
#Memory Usage: 13.6 MB, less than 98.49% of Python3 online submissions for Sort Colors.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l > 1:
            middle = l // 2
            left_part = nums[:middle]
            right_part = nums[middle:]
            self.sortColors(left_part)
            self.sortColors(right_part)
            i=j=k = 0
            while i < len(left_part) and j < len(right_part):
                if left_part[i] < right_part[j]:
                    nums[k] = left_part[i]
                    i += 1
                else:
                    nums[k] = right_part[j]
                    j += 1
                k += 1
            while i < len(left_part):
                nums[k] = left_part[i]
                i += 1
                k += 1
            while j < len(right_part):
                nums[k] = right_part[j]
                j += 1
                k += 1
