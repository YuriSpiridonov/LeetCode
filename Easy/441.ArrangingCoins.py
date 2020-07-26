"""
    You have a total of n coins that you want to form in a staircase shape, 
    where every k-th row must have exactly k coins.
    Given n, find the total number of full staircase rows that can be formed.
    n is a non-negative integer and fits within the range of a 32-bit signed 
    integer.

    Example:
    n = 8
    The coins can form the following rows:
    ¤
    ¤ ¤
    ¤ ¤ ¤
    ¤ ¤
    Because the 4th row is incomplete, we return 3.
"""
#Difficulty: Easy
#1336 / 1336 test cases passed.
#Runtime: 852 ms
#Memory Usage: 13.8 MB

#Runtime: 852 ms, faster than 47.02% of Python3 online submissions for Arranging Coins.
#Memory Usage: 13.8 MB, less than 54.40% of Python3 online submissions for Arranging Coins.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while i < n:
            i += 1
            n -= i
        return i
