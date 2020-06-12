"""
    Implement pow(x, n), which calculates x raised to the power n (x**n).
    
    Example:
    Input: 2.10000, 3
    Output: 9.26100
    
    Example:
    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25
    
    Note:
        - -100.0 < x < 100.0
        - n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""
#Difficulty: Medium   
#304 / 304 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14 MB
      
#Runtime: 24 ms, faster than 92.57% of Python3 online submissions for Pow(x, n).
#Memory Usage: 14 MB, less than 15.17% of Python3 online submissions for Pow(x, n).        
      
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n: return 1
        power = self.myPow(x, int(n/2))
        if n % 2 == 0:
            return power * power
        else:
            return power * power / x if n < 0 else power * power * x
