'''
    Given a positive integer n, find the smallest integer 
    which has exactly the same digits existing in the integer 
    n and is greater in value than n. If no such positive 
    integer exists, return -1.

    Note that the returned integer should fit in 32-bit integer, 
    if there is a valid answer but it does not fit in 32-bit 
    integer, return -1.

    Example:
    Input: n = 12
    Output: 21

    Example:
    Input: n = 21
    Output: -1

    Constraints:
        - 1 <= n <= 2^31 - 1
'''
#Difficulty: Medium
#36 / 36 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.1 MB

#Runtime: 32 ms, faster than 39.70% of Python3 online submissions for Next Greater Element III.
#Memory Usage: 14.1 MB, less than 56.67% of Python3 online submissions for Next Greater Element III.

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        m = 0
        length = -1
        digits = []
        max_value = 2 ** 31 - 1
        while n:
            digits.insert(0, n%10)
            n //= 10
            length += 1
        while length > 0:
            if digits[length] > digits[length-1]:
                temp1 = digits[:length-1]
                temp2 = digits[length-1:]
                temp1.append(temp2.pop(temp2.index(min(i for i in temp2 if i > temp2[0]))))
                temp1.extend(sorted(temp2))
                for digit in temp1:
                    m = m * 10 + digit
                break
            length -= 1
        return m if m and m <= max_value else -1
