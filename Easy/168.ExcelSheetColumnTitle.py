"""
    Given a positive integer, return its corresponding column title as appear 
    in an Excel sheet.

    For example:
        
            1 -> A
            2 -> B
            3 -> C
            ...
            26 -> Z
            27 -> AA
            28 -> AB 
            ...

    Example:
    Input: 701
    Output: "ZY"
"""
#Difficulty: Easy
#18 / 18 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.1 MB

#Runtime: 28 ms, faster than 73.06% of Python3 online submissions for Excel Sheet Column Title.
#Memory Usage: 14.1 MB, less than 99.90% of Python3 online submissions for Excel Sheet Column Title.

class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        if n <= 26:
            s += chr(64+n)
        while n > 26:
            m = n % 26
            n = n // 26
            if not m:
                m = 26
                n -= 1
            if n > 26:
                s += chr(64+m)
                continue
            s +=  chr(64+m)
            s +=  chr(64+n)
        return s[::-1]   
