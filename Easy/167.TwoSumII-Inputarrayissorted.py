"""
    Given an array of integers that is already sorted in ascending order, find 
    two numbers such that they add up to a specific target number.
    The function twoSum should return indices of the two numbers such that they 
    add up to the target, where index1 must be less than index2.

    Note:
    - Your returned answers (both index1 and index2) are not zero-based.
    - You may assume that each input would have exactly one solution and you may 
    not use the same element twice.

    Example:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
#Difficulty: Easy
#17 / 17 test cases passed.
#Runtime: 52 ms
#Memory Usage: 14.1 MB

#Runtime: 52 ms, faster than 99.27% of Python3 online submissions for Two Sum II - Input array is sorted.
#Memory Usage: 14.1 MB, less than 5.80% of Python3 online submissions for Two Sum II - Input array is sorted.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = sorted(list(set(numbers)))
        for n in s:
            if target - n in numbers:
                i = numbers.index(n) + 1
                j = i + numbers[i:].index(target - n) + 1
                return [i, j]
