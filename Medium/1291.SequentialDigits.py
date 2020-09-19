"""
    An integer has sequential digits if and only if each digit in the number is 
    one more than the previous digit.
    Return a sorted list of all the integers in the range [low, high] inclusive 
    that have sequential digits.

    Example:
    Input: low = 100, high = 300
    Output: [123,234]

    Example:
    Input: low = 1000, high = 13000
    Output: [1234,2345,3456,4567,5678,6789,12345]

    Constraints:
        - 10 <= low <= high <= 10^9
"""
#Difficulty: Medium
#21 / 21 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.8 MB

#Runtime: 28 ms, faster than 77.18% of Python3 online submissions for Sequential Digits.
#Memory Usage: 13.8 MB, less than 52.82% of Python3 online submissions for Sequential Digits.

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        i = 0
        j = len(str(low))
        num = 0
        result = [] 
        digits = "1234567890"
        length = len(digits)
        while num < high:
            num = int(digits[i:i+j])
            if num in range(low, high+1):
                result.append(num)
            i += 1
            if i + j >= length:
                j += 1
                i = 0
        return result
