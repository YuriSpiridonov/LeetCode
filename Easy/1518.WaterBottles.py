"""
    Given numBottles full water bottles, you can exchange numExchange empty 
    water bottles for one full water bottle.
    The operation of drinking a full water bottle turns it into an empty bottle.
    Return the maximum number of water bottles you can drink.

    Example:
    Input: numBottles = 15, numExchange = 4
    Output: 19
    Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
    Number of water bottles you can drink: 15 + 3 + 1 = 19.

    Constraints:
        - 1 <= numBottles <= 100
        - 2 <= numExchange <= 100
"""
#Difficulty: Easy
#64 / 64 test cases passed.
#Runtime: 16 ms
#Memory Usage: 13.9 MB

#Runtime: 16 ms, faster than 99.90% of Python3 online submissions for Water Bottles.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Water Bottles.

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            emptyExchange = numBottles // numExchange
            emptyNotExchange = numBottles % numExchange
            numBottles = emptyExchange + emptyNotExchange
            total += emptyExchange
        return total
