"""
    (This problem is an interactive problem.)
    You may recall that an array A is a mountain array if and only if:
    - A.length >= 3
    - There exists some i with 0 < i < A.length - 1 such that:
            - A[0] < A[1] < ... A[i-1] < A[i]
            - A[i] > A[i+1] > ... > A[A.length - 1]
    Given a mountain array mountainArr, return the minimum index such that 
    mountainArr.get(index) == target.  
    If such an index doesn't exist, return -1.
    
    You can't access the mountain array directly.  You may only access the 
    array using a MountainArray interface:
        - MountainArray.get(k) returns the element of the array at index k 
          (0-indexed).
        - MountainArray.length() returns the length of the array.
    
    Submissions making more than 100 calls to MountainArray.get will be judged 
    Wrong Answer.  Also, any solutions that attempt to circumvent the judge 
    will result in disqualification.
    
    Example:
    Input: array = [1,2,3,4,5,3,1], target = 3
    Output: 2
    Explanation: 3 exists in the array, at index=2 and index=5. 
    Return the minimum index, which is 2.
    
    Example:
    Input: array = [0,1,2,4,2,1], target = 3
    Output: -1
    Explanation: 3 does not exist in the array, so we return -1.
    
    Constraints:
        - 3 <= mountain_arr.length() <= 10000
        - 0 <= target <= 10^9
        - 0 <= mountain_arr.get(index) <= 10^9
"""
#Difficulty: Hard
#77 / 77 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14.5 MB

#Runtime: 24 ms, faster than 93.77% of Python3 online submissions for Find in Mountain Array.
#Memory Usage: 14.5 MB, less than 68.70% of Python3 online submissions for Find in Mountain Array.

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.peakBinarySearch(mountain_arr)
        result = self.targetBinarySearchLeft(mountain_arr, target, peak)
        if -1 == result:
            result = self.targetBinarySearchRight(mountain_arr, target, peak)
        return result
        
    def targetBinarySearchLeft(self, mountain_arr, target, peak):
        '''Searching target on the left of the mountain peak'''
        left = 0
        right = peak
        while left <= right:
            middle = (left + right) // 2
            if mountain_arr.get(middle) == target:
                return middle
            if mountain_arr.get(middle) > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1
    
    def targetBinarySearchRight(self, mountain_arr, target, peak):
        '''Searching target on the right of the mountain peak'''
        left = peak
        right = mountain_arr.length() - 1
        while left <= right:
            middle = (left + right) // 2
            if mountain_arr.get(middle) == target:
                return middle
            if mountain_arr.get(middle) < target:
                right = middle - 1
            else:
                left = middle + 1
        return -1
    
    def peakBinarySearch(self, mountain_arr):
        '''Searching mountain peak'''
        left = 1
        right = mountain_arr.length() - 1
        while left <= right:
            middle = (left + right) // 2
            mid_ele = mountain_arr.get(middle)
            left_ele = mountain_arr.get(middle-1)
            right_ele = mountain_arr.get(middle+1)
            if left_ele < mid_ele > right_ele:
                return middle
            if left_ele > mid_ele > right_ele:
                right = middle - 1
            else:
                left = middle + 1
