"""
    We have n chips, where the position of the ith chip is position[i].

    We need to move all the chips to the same position. In one step, we can 
    change the position of the ith chip from position[i] to:

    position[i] + 2 or position[i] - 2 with cost = 0.
    position[i] + 1 or position[i] - 1 with cost = 1.
    Return the minimum cost needed to move all the chips to the same position.

    Example:
    Input: position = [1,2,3]
    Output: 1
    Explanation: First step: Move the chip at position 3 to position 1 with 
                 cost = 0.
                 Second step: Move the chip at position 2 to position 1 with 
                 cost = 1.
                 Total cost is 1.

    Example:
    Input: position = [2,2,2,3,3]
    Output: 2
    Explanation: We can move the two chips at poistion 3 to position 2. 
                 Each move has cost = 1. The total cost = 2.

    Example:
    Input: position = [1,1000000000]
    Output: 1

    Constraints:
        - 1 <= position.length <= 100
        - 1 <= position[i] <= 10^9
"""
#Difficulty: Easy
#51 / 51 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.1 MB

#Runtime: 32 ms, faster than 63.46% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
#Memory Usage: 14.1 MB, less than 99.86% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        even = 0
        for pos in position:
            if pos % 2:
                odd += 1
            else:
                even += 1
        return min(odd, even)
