"""
    Given an array of integers arr, write a function that returns true if and 
    only if the number of occurrences of each value in the array is unique.

    Example:
    Input: arr = [1,2,2,1,1,3]
    Output: true
    Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two 
                 values have the same number of occurrences.

    Example:
    Input: arr = [1,2]
    Output: false

    Example:
    Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
    Output: true

    Constraints:
        - 1 <= arr.length <= 1000
        - -1000 <= arr[i] <= 1000
"""
#Difficulty: Easy
#63 / 63 test cases passed.
#Runtime: 48 ms
#Memory Usage: 13.8 MB

#Runtime: 48 ms, faster than 39.33% of Python3 online submissions for Unique Number of Occurrences.
#Memory Usage: 13.8 MB, less than 92.46% of Python3 online submissions for Unique Number of Occurrences.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        digits = {}
        for d in arr:
            if d not in digits:
                digits[d] = 0
            digits[d] += 1
        return len(digits.keys()) == len(set(digits.values()))
