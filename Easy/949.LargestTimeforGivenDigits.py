"""
    Given an array of 4 digits, return the largest 24 hour time that can be
    made.
    The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting 
    from 00:00, a time is larger if more time has elapsed since midnight.
    Return the answer as a string of length 5.  If no valid time can be made, 
    return an empty string.

    Example:
    Input: [1,2,3,4]
    Output: "23:41"

    Example:
    Input: [5,5,5,5]
    Output: ""

    Note:
        1. A.length == 4
        2. 0 <= A[i] <= 9
"""
#Difficulty: Easy
#172 / 172 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.9 MB

#Runtime: 28 ms, faster than 92.89% of Python3 online submissions for Largest Time for Given Digits.
#Memory Usage: 13.9 MB, less than 50.65% of Python3 online submissions for Largest Time for Given Digits.

import itertools

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        result = ''
        combinations = itertools.permutations(A, 4)
        for combo in combinations:
            if combo[0] * 10 + combo[1] < 24 and combo[2] * 10 + combo[3] < 60:
                 result = max(result, str(combo[0]) + str(combo[1]) + ':' + str(combo[2]) + str(combo[3]))
        return result
