"""
    Given a non-empty array of digits representing a non-negative integer, 
    plus one to the integer.
    The digits are stored such that the most significant digit is at the head 
    of the list, and each element in the array contain a single digit.
    You may assume the integer does not contain any leading zero, except the 
    number 0 itself.
    
    Example:
    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
"""
#Difficulty: Easy
#109 / 109 test cases passed.
#Runtime: 32 ms
#Memory Usage: 13.6 MB

#Runtime: 32 ms, faster than 63.07% of Python3 online submissions for Plus One.
#Memory Usage: 13.6 MB, less than 5.13% of Python3 online submissions for Plus One.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = 0
        l = len(digits)
        for digit in digits:
            d = d * 10 + digit
        d+=1
        digits.clear()
        while d:
            number = d % 10
            digits.insert(0,number)
            d//=10
        while len(digits) < l:
            digits.insert(0,0)
        return digits
