'''
    You are given an integer array cost where cost[i] is the 
    cost of ith step on a staircase. Once you pay the cost, 
    you can either climb one or two steps.

    You can either start from the step with index 0, or the 
    step with index 1.

    Return the minimum cost to reach the top of the floor.

    Example:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: Cheapest is: start on cost[1], pay that 
                 cost, and go to the top.

    Example:
    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: Cheapest is: start on cost[0], and only 
                 step on 1s, skipping cost[3].

    Constraints:
        - 2 <= cost.length <= 1000
        - 0 <= cost[i] <= 999
'''
#Difficulty: Easy
#279 / 279 test cases passed.
#Runtime: 64 ms
#Memory Usage: 14.5 MB

#Runtime: 64 ms, faster than 23.75% of Python3 online submissions for Min Cost Climbing Stairs.
#Memory Usage: 14.5 MB, less than 44.78% of Python3 online submissions for Min Cost Climbing Stairs.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev0 = 0
        prev1 = 0
        count = 0
        for i in range(1, len(cost)):
            count = min(prev0+cost[i-1], prev1+cost[i])
            prev0, prev1 = prev1, count
        return count
