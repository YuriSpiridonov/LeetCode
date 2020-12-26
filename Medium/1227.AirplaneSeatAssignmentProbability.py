'''
    n passengers board an airplane with exactly n seats. The 
    first passenger has lost the ticket and picks a seat 
    randomly. But after that, the rest of passengers will:
        - Take their own seat if it is still available, 
        - Pick other seats randomly when they find their 
          seat occupied 

    What is the probability that the n-th person can get his 
    own seat?

    Example:
    Input: n = 1
    Output: 1.00000
    Explanation: The first person can only get the first seat.

    Example:
    Input: n = 2
    Output: 0.50000
    Explanation: The second person has a probability of 0.5 
                 to get the second seat (when first person 
                 gets the first seat).

    Constraints:
        - 1 <= n <= 10^5
'''
#Difficulty: Medium
#100 / 100 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.2 MB

#Runtime: 32 ms, faster than 49.09% of Python3 online submissions for Airplane Seat Assignment Probability.
#Memory Usage: 14.2 MB, less than 23.33% of Python3 online submissions for Airplane Seat Assignment Probability.

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 0.5 if n > 1 else 1
