"""
    Given an array of integers, 1 <= a[i] <= n (n = size of array), some 
    elements appear twice and others appear once.
    Find all the elements that appear twice in this array.
    Could you do it without extra space and in O(n) runtime?

    Example:
    Input:
    [4,3,2,7,8,2,3,1]
    Output:
    [2,3]
"""
#Difficulty: Medium
#28 / 28 test cases passed.
#Runtime: 348 ms
#Memory Usage: 23.5 MB

#Runtime: 348 ms, faster than 99.23% of Python3 online submissions for Find All Duplicates in an Array.
#Memory Usage: 23.5 MB, less than 5.59% of Python3 online submissions for Find All Duplicates in an Array.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = set()
        visited = set()
        for num in nums:
            if num in visited:
                duplicates.add(num)
            visited.add(num)
        return duplicates
