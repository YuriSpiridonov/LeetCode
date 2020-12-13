'''
    Roman numerals are represented by seven different symbols: 
    I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

    For example, 2 is written as II in Roman numeral, just two 
    one's added together. 12 is written as XII, which is simply 
    X + II. The number 27 is written as XXVII, which is 
    XX + V + II.

    Roman numerals are usually written largest to smallest from 
    left to right. However, the numeral for four is not IIII. 
    Instead, the number four is written as IV. Because the one 
    is before the five we subtract it making four. The same 
    principle applies to the number nine, which is written as IX. 
    There are six instances where subtraction is used:

        - I can be placed before V (5) and X (10) to make 4 
          and 9. 
        - X can be placed before L (50) and C (100) to make 40 
          and 90. 
        - C can be placed before D (500) and M (1000) to make 
          400 and 900.

    Given a roman numeral, convert it to an integer.

    Example:
    Input: s = "III"
    Output: 3

    Example:
    Input: s = "IV"
    Output: 4

    Example:
    Input: s = "IX"
    Output: 9

    Example:
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.

    Example:
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    Constraints:
        - 1 <= s.length <= 15
        - s contains only the characters 
          ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        - It is guaranteed that s is a valid roman numeral 
          in the range [1, 3999].
'''
#Dfficulty: Easy
#3999 / 3999 test cases passed.
#Runtime: 52 ms
#Memory Usage: 14.4 MB

#Runtime: 52 ms, faster than 34.70% of Python3 online submissions for Roman to Integer.
#Memory Usage: 14.4 MB, less than 10.59% of Python3 online submissions for Roman to Integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0
        nums = {'I': 1, 'IV': 4, 'V': 5, 'VI': 6, 'IX': 9,
                'X': 10, 'XL': 40, 'L': 50, 'LX': 60, 
                'XC': 90,'C': 100, 'CD': 400, 'D': 500, 
                'DC': 600, 'CM': 900, 'M': 1000}
        while s:
            d = s[:2]
            s = s[2:]
            if d in nums:
                n += nums[d]
            else:
                d1, d2 = d[0], d[1]
                n += nums[d1]
                if d2:
                    s = d2 + s
        return n
