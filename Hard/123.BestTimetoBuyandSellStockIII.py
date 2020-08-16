"""
    Say you have an array for which the ith element is the price of a given 
    stock on day i.
    Design an algorithm to find the maximum profit. You may complete at most 
    two transactions.
    Note: You may not engage in multiple transactions at the same time (i.e., 
    you must sell the stock before you buy again).

    Example:
    Input: [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), 
                 profit = 3-0 = 3.
                 Then buy on day 7 (price = 1) and sell on day 8 (price = 4), 
                 profit = 4-1 = 3.

    Example:
    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), 
                 profit = 5-1 = 4.
                 Note that you cannot buy on day 1, buy on day 2 and sell them 
                 later, as you are
                 engaging multiple transactions at the same time. You must sell 
                 before buying again.

    Example:
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
#Difficulty: Hard
#200 / 200 test cases passed.
#Runtime: 76 ms
#Memory Usage: 15.1 MB

#Runtime: 76 ms, faster than 90.91% of Python3 online submissions for Best Time to Buy and Sell Stock III.
#Memory Usage: 15.1 MB, less than 79.35% of Python3 online submissions for Best Time to Buy and Sell Stock III.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        transaction_one = float(inf)
        transaction_two = float(inf)
        current_profit = 0
        total_profit = 0
        for price in prices:
            transaction_one = min(transaction_one, price)
            current_profit = max(current_profit, price - transaction_one)
            transaction_two = min(transaction_two, price - current_profit)
            total_profit = max(total_profit, price - transaction_two)
        return total_profit
