"""
    Given the array nums, for each nums[i] find out how many numbers in the 
    array are smaller than it. That is, for each nums[i] you have to count the 
    number of valid j's such that j != i and nums[j] < nums[i].
    Return the answer in an array.
    
    Example:
    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]
    Explanation: 
                - For nums[0]=8 there exist four smaller numbers than it 
                  (1, 2, 2 and 3). 
                - For nums[1]=1 does not exist any smaller number than it.
                - For nums[2]=2 there exist one smaller number than it (1). 
                - For nums[3]=2 there exist one smaller number than it (1). 
                - For nums[4]=3 there exist three smaller numbers than it 
                  (1, 2 and 2).
    
    Constraints:
        - 2 <= nums.length <= 500
        - 0 <= nums[i] <= 100
"""
#Difficulty: Easy
#103 / 103 test cases passed.
#Runtime: 92 ms
#Memory Usage: 13.7 MB

#Runtime: 92 ms, faster than 56.51% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
#Memory Usage: 13.7 MB, less than 93.98% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        return [len(sorted_nums[:sorted_nums.index(n)]) for n in nums]
