"""
    A peak element is an element that is greater than its neighbors.
    Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element 
    and return its index.
    The array may contain multiple peaks, in that case return the index to any 
    one of the peaks is fine.
    You may imagine that nums[-1] = nums[n] = -∞.
    
    Example:
    Input: nums = [1,2,1,3,5,6,4]
    Output: 1 or 5 
    Explanation: Your function can return either index number 1 where the peak 
                 element is 2, or index number 5 where the peak element is 6.
    
    Follow up: Your solution should be in logarithmic complexity.
"""
#Difficulty: Medium
#59 / 59 test cases passed.
#Runtime: 40 ms
#Memory Usage: 13.9 MB

#Runtime: 40 ms, faster than 92.30% of Python3 online submissions for Find Peak Element.
#Memory Usage: 13.9 MB, less than 81.39% of Python3 online submissions for Find Peak Element.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        set_of_nums = sorted(set(nums), reverse = True)
        index = 0
        m = set_of_nums[index]
        i = nums.index(m)
        if i == 0 or i == len(nums) - 1:
            return i
        else:
            while True:
                if nums[i-1] <= nums[i] >= nums[i+1]:
                    return i
                else:
                    index+=1
                    m = set_of_nums[index]
                    i = nums.index(m)
