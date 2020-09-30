"""
    Given an array of numbers arr. A sequence of numbers is called an 
    arithmetic progression if the difference between any two consecutive 
    elements is the same.
    Return true if the array can be rearranged to form an arithmetic 
    progression, otherwise, return false.

    Example:
    Input: arr = [3,5,1]
    Output: true
    Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with 
                 ifferences 2 and -2 respectively, between each consecutive 
                 elements.

    Example:
    Input: arr = [1,2,4]
    Output: false
    Explanation: There is no way to reorder the elements to obtain an 
                 arithmetic progression.

    Constraints:
        - 2 <= arr.length <= 1000
        - -10^6 <= arr[i] <= 10^6
"""
#Difficulty: Easy
#102 / 102 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14.2 MB

#Runtime: 36 ms, faster than 90.39% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
#Memory Usage: 14.2 MB, less than 6.83% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True
