"""
    Given an integer n, add a dot (".") as the thousands separator and return 
    it in string format.

    Example:
    Input: n = 987
    Output: "987"

    Example:
    Input: n = 1234
    Output: "1.234"

    Example:
    Input: n = 123456789
    Output: "123.456.789"

    Example:
    Input: n = 0
    Output: "0"
    
    Constraints:
        - 0 <= n < 2^31
"""
#Difficulty: Easy
#69 / 69 test cases passed.
#Runtime: 52 ms
#Memory Usage: 13.9 MB

#Runtime: 52 ms, faster than 25.00% of Python3 online submissions for Thousand Separator.
#Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Thousand Separator.

class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        l = len(s)
        nums = []
        while s:
            if l > 2:
                l -= 3
            else:
                nums.insert(0, s[:l])
                break
            nums.insert(0, s[l:])
            s = s[:l]
        return '.'.join(nums)
