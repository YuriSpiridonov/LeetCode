"""
    Given a sorted array nums, remove the duplicates in-place such that each 
    element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this by 
    modifying the input array in-place with O(1) extra memory.
    
    Example:
    Given nums = [0,0,1,1,1,2,2,3,3,4],
    Your function should return length = 5, with the first five elements of 
    nums being modified to 0, 1, 2, 3, and 4 respectively.
    It doesn't matter what values are set beyond the returned length.
    
    Clarification:
    Confused why the returned value is an integer but your answer is an array?
    Note that the input array is passed in by reference, which means 
    modification to the input array will be known to the caller as well.
"""
#---Solutin 1---
#Difficulty: Easy
#161 / 161 test cases passed.
#Runtime: 1480 ms
#Memory Usage: 15.5 MB

#Runtime: 1480 ms, faster than 5.04% of Python3 online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 15.5 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        n = nums[-1]
        for num in nums[-2::-1]:
            if num == n:
                nums.pop(nums.index(num))
            else:
                n = num
        return len(nums)
#---End of Solution 1---

#---Solutin 2---
#Difficulty: Easy
#161 / 161 test cases passed.
#Runtime: 92 ms
#Memory Usage: 15.3 MB

#Runtime: 92 ms, faster than 43.66% of Python3 online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 15.3 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        l = len(nums)
        n = nums[i]
        indices = list()
        for j in range(i+1, l):
            if nums[j] == n:
                indices.append(j)
            n = nums[j]
        for j in reversed(indices):
            nums.pop(j)
        return len(nums)
#---End of Solution 2---

#---Solution 3---
#Difficulty: Easy
#161 / 161 test cases passed.
#Runtime: 88 ms
#Memory Usage: 15.7 MB

#Runtime: 88 ms, faster than 57.80% of Python3 online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 15.7 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        n = nums[0]
        i = list()
        for j in range(1, len(nums)):
            if nums[j] == n:
                i.append(j)
            n = nums[j]
        i.reverse()
        for j in i:
            nums.pop(j)
        return len(nums)
#---End of Solution 3---

#---Solution 4---
#Difficulty: Easy
#161 / 161 test cases passed.
#Runtime: 84 ms
#Memory Usage: 15.6 MB
        
#Runtime: 84 ms, faster than 76.46% of Python3 online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 15.6 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        n = nums[i]
        for j in range(i+1, len(nums)):
            if n != nums[j]:
                nums[i+1] = nums[j]
                i += 1
                n = nums[j]
        nums = nums[:i+1]
        return len(nums)
#---End of Solution 4---

#---Solution 4.1---
#Difficulty: Easy
#161 / 161 test cases passed.
#Runtime: 76 ms
#Memory Usage: 15.6 MB
        
#Runtime: 76 ms, faster than 96.62% of Python3 online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 15.6 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.  
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        n = nums[i]
        for j in range(i+1, len(nums)):
            if n != nums[j]:
                nums[i+1] = nums[j]
                i += 1
                n = nums[j]
        nums = nums[:i+1]
        return i+1
#---End of Solution 4.1---

#---Solution 5---
#Difficulty: Easy
#161 / 161 test cases passed.
#Runtime: 84 ms
#Memory Usage: 15.5 MB

#Runtime: 84 ms, faster than 76.46% of Python3 online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 15.5 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
#---End of Solution 5---
