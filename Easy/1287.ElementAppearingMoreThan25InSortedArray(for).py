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
#Runtime: 180 ms
#Memory Usage: 15.9 MB

#Runtime: 180 ms, faster than 11.20% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
#Memory Usage: 15.9 MB, less than 12.26% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        nums = {}
        result = arr[0]
        for num in arr:
            if num not in nums:
                nums[num] = 0
            nums[num] += 1
            if nums[num] >= length // 4:
                result = result if nums[result] > nums[num] else num
        return result
