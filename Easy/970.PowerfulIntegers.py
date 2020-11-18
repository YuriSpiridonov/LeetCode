"""
    Given two positive integers x and y, an integer is powerful if it is equal 
    to x^i + y^j for some integers i >= 0 and j >= 0.

    Return a list of all powerful integers that have value less than or equal 
    to bound.

    You may return the answer in any order.  In your answer, each value should 
    occur at most once.

    Example:
    Input: x = 2, y = 3, bound = 10
    Output: [2,3,4,5,7,9,10]
    Explanation: 
                2 = 2^0 + 3^0
                3 = 2^1 + 3^0
                4 = 2^0 + 3^1
                5 = 2^1 + 3^1
                7 = 2^2 + 3^1
                9 = 2^3 + 3^0
                10 = 2^0 + 3^2

    Example:
    Input: x = 3, y = 5, bound = 15
    Output: [2,4,6,8,10,14]

    Note:
        - 1 <= x <= 100
        - 1 <= y <= 100
        - 0 <= bound <= 10^6
"""
#Difficulty: Easy
#93 / 93 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14 MB

#Runtime: 32 ms, faster than 61.64% of Python3 online submissions for Powerful Integers.
#Memory Usage: 14 MB, less than 63.29% of Python3 online submissions for Powerful Integers.

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        for j in range(20):
            for i in range(20):
                res = x**i + y**j
                if res <= bound:
                    result.add(res)
                else:
                    break
        return result
