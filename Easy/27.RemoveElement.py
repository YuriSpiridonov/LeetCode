"""
    Given an array nums and a value val, remove all instances of that value 
    in-place and return the new length.
    Do not allocate extra space for another array, you must do this by modifying 
    the input array in-place with O(1) extra memory.
    The order of elements can be changed. It doesn't matter what you leave 
    beyond the new length.
    
    Example:
    Given nums = [3,2,2,3], val = 3,
    Your function should return length = 2, with the first two elements of nums 
    being 2.
    It doesn't matter what you leave beyond the returned length.
"""
#Difficulty: Easy
#113 / 113 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.6 MB

#Runtime: 28 ms, faster than 88.43% of Python3 online submissions for Remove Element.
#Memory Usage: 13.6 MB, less than 6.06% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)-1
        while val in nums:
            if nums[length] == val:
                nums.pop(length)
            length-=1    
        return len(nums)
