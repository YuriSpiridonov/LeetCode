"""
    Given two non-negative integers low and high. Return the count of odd 
    numbers between low and high (inclusive).

    Example:
    Input: low = 3, high = 7
    Output: 3
    Explanation: The odd numbers between 3 and 7 are [3,5,7].

    Constraints:
        - 0 <= low <= high <= 10^9
"""
#Difficulty: Easy
#84 / 84 test cases passed.
#Runtime: 24 ms
#Memory Usage: 13.9 MB

#Runtime: 24 ms, faster than 75.00% of Python3 online submissions for Count Odd Numbers in an Interval Range.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Count Odd Numbers in an Interval Range.

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return 1 + (high + 1 - low) // 2 if low % 2 and high % 2 else (high + 1 - low) // 2 
