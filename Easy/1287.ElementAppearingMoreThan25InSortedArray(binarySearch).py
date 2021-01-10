'''
    Given an integer array sorted in non-decreasing order, 
    there is exactly one integer in the array that occurs 
    more than 25% of the time.

    Return that integer.

    Example:
    Input: arr = [1,2,2,6,6,6,6,7,10]
    Output: 6

    Constraints:
        - 1 <= arr.length <= 10^4
        - 0 <= arr[i] <= 10^5
'''
#Difficulty: Easy
#18 / 18 test cases passed.
#Runtime: 120 ms
#Memory Usage: 15.9 MB

#Runtime: 120 ms, faster than 14.93% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
#Memory Usage: 15.9 MB, less than 12.26% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.

class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        nums = set(arr)
        if length == 1:
            return arr[0]
        for num in nums:
            n = self.binarySearch(arr, num, length)
            if n:
                return n
    
    def binarySearch(self, arr: int, num: int, length: int) -> int:
        l = 0
        r = length - 1
        q = (length+1)//4
        while l < r:
            m = (l+r) // 2
            if arr[m] == num and arr[min(length-1, m+q)] == num:
                return num
            elif num > arr[m]:
                l = m + 1
            else:
                r = m - 1
