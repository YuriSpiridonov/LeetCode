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
#Algorithm: Selection Sort
#87 / 87 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.8 MB

#Runtime: 28 ms, faster than 92.50% of Python3 online submissions for Sort Colors.
#Memory Usage: 13.8 MB, less than 49.24% of Python3 online submissions for Sort Colors.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums) 
        i = 0
        for i in range(l):
            index = i
            for j in range(i+1, l):
                if nums[index] > nums[j]:
                    index = j
            nums[i], nums[index] = nums[index], nums[i]
