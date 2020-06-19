"""
    Given two integer arrays of equal length target and arr.
    
    In one step, you can select any non-empty sub-array of arr and reverse it. 
    You are allowed to make any number of steps.
    
    Return True if you can make arr equal to target, or False otherwise.
    
    Example:
    Input: target = [1,2,3,4], arr = [2,4,1,3]
    Output: true
    Explanation: You can follow the next steps to convert arr to target:
                 1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
                 2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
                 3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
                 There are multiple ways to convert arr to target, 
                 this is not the only way to do so.
    
    Constraints:
        - target.length == arr.length
        - 1 <= target.length <= 1000
        - 1 <= target[i] <= 1000
        - 1 <= arr[i] <= 1000
"""
#Difficulty: Easy
#102 / 102 test cases passed.
#Runtime: 72 ms
#Memory Usage: 14.1 MB

#Runtime: 72 ms, faster than 98.81% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.
#Memory Usage: 14.1 MB, less than 24.84% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.    
    
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sum(target) == sum(arr) and set(target) == set(arr)
