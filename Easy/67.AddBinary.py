"""
    Given two binary strings, return their sum (also a binary string).
    The input strings are both non-empty and contains only characters 1 or 0.
    
    Example:
    Input: a = "11", b = "1"
    Output: "100"
"""
#Difficulty: Easy
#294 / 294 test cases passed.
#Runtime: 32 ms
#Memory Usage: 13.8 MB

#Runtime: 32 ms, faster than 66.60% of Python3 online submissions for Add Binary.
#Memory Usage: 13.8 MB, less than 5.41% of Python3 online submissions for Add Binary.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a[::-1])
        b = list(b[::-1])
        length_a = len(a)
        length_b = len(b)
        temp = '0'
        i = 0
        if length_a < length_b: 
            a += ['0'] * (length_b - length_a)
            length_a = len(a)
        else: 
            b += ['0'] * (length_a - length_b)
        while True:
            if int(a[i]) + int(b[i]) + int(temp) == 3:
                a[i] = '1'
                temp = '1'
            elif int(a[i]) + int(b[i]) + int(temp) == 2:
                a[i] = '0'
                temp = '1'
            elif int(a[i]) + int(b[i]) + int(temp) == 1:
                a[i] = '1'
                temp = '0'
            else:
                a[i] = '0'
                temp = '0'
            i += 1
            if i == length_a and temp == '1':
                a.append(temp)
                break
            if i == length_a:
                break
        return ''.join(a[::-1])
