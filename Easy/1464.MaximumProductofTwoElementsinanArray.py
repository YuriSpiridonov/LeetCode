"""
    Given the array of integers nums, you will choose two different indices i 
    and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
    
    Example:
    Input: nums = [3,4,5,2]
    Output: 12 
    Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you 
                 will get the maximum value, that is, 
                 (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
    
    Constraints:
        - 2 <= nums.length <= 500
        - 1 <= nums[i] <= 10^3
"""
#Difficulty: Easy
#104 / 104 test cases passed.
#Runtime: 44 ms
#Memory Usage: 13.8 MB

#Runtime: 44 ms, faster than 97.04% of Python3 online submissions for Maximum Product of Two Elements in an Array.
#Memory Usage: 13.8 MB, less than 84.74% of Python3 online submissions for Maximum Product of Two Elements in an Array.    
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2] - 1) * (nums[-1] - 1)
