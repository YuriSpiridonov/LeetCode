"""
    Given an array of integers, find if the array contains any duplicates.
    Your function should return true if any value appears at least twice in 
    the array, and it should return false if every element is distinct.

    Example:
    Input: [1,1,1,3,3,4,3,2,4,2]
    Output: true
"""
#Difficulty: Easy
#18 / 18 test cases passed.
#Runtime: 144 ms
#Memory Usage: 20.1 MB

#Runtime: 144 ms, faster than 31.07% of Python3 online submissions for Contains Duplicate.
#Memory Usage: 20.1 MB, less than 27.68% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num in d.keys():
                return d[num]
            d[num] = True
        return False
