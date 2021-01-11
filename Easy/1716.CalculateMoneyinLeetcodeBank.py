'''
    Hercy wants to save money for his first car. He puts 
    money in the Leetcode bank every day.

    He starts by putting in $1 on Monday, the first day. 
    Every day from Tuesday to Sunday, he will put in $1 
    more than the day before. On every subsequent Monday, 
    he will put in $1 more than the previous Monday.

    Given n, return the total amount of money he will have 
    in the Leetcode bank at the end of the nth day.

    Example:
    Input: n = 4
    Output: 10
    Explanation: After the 4th day, the total is 
                 1 + 2 + 3 + 4 = 10.

    Example:
    Input: n = 10
    Output: 37
    Explanation: After the 10th day, the total is 
                 (1 + 2 + 3 + 4 + 5 + 6 + 7) + 
                 (2 + 3 + 4) = 37. 
                 Notice that on the 2nd Monday, Hercy only 
                 puts in $2.

    Example:
    Input: n = 20
    Output: 96
    Explanation: After the 20th day, the total is 
                 (1 + 2 + 3 + 4 + 5 + 6 + 7) + 
                 (2 + 3 + 4 + 5 + 6 + 7 + 8) + (
                     3 + 4 + 5 + 6 + 7 + 8) = 96.

    Constraints:
        - 1 <= n <= 1000
'''
#Difficulty: Easy
#106 / 106 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14.1 MB

#Runtime: 40 ms, faster than 75.00% of Python3 online submissions for Calculate Money in Leetcode Bank.
#Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Calculate Money in Leetcode Bank.

class Solution:
    def totalMoney(self, n: int) -> int:
        i = 1
        total = 0
        deposit = 1
        while n:
            total += deposit
            if not i % 7 or not i % n:
                deposit -= 5
                n -= i
                i = 1
            else:
                deposit += 1
                i += 1
        return total
