"""
    A self-dividing number is a number that is divisible by every digit it 
    contains.
    For example, 128 is a self-dividing number because 128 % 1 == 0, 
                                                128 % 2 == 0, and 128 % 8 == 0.
    Also, a self-dividing number is not allowed to contain the digit zero.
    Given a lower and upper number bound, output a list of every possible self 
    dividing number, including the bounds if possible.

    Example:
    Input: 
    left = 1, right = 22
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

    Note:
        - The boundaries of each input argument are 1 <= left <= right <= 10000.
"""
#Difficulty: Easy
#31 / 31 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14.1 MB

#Runtime: 36 ms, faster than 98.67% of Python3 online submissions for Self Dividing Numbers.
#Memory Usage: 14.1 MB, less than 5.05% of Python3 online submissions for Self Dividing Numbers.

class Solution:
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for number in range(left, right+1):
            number = self.selfDividingNumber(number)
            if number:
                result.append(number)
        return result

    def selfDividingNumber(self, number):
        temp = number
        while temp:
            n = temp % 10
            temp //= 10
            if n == 0 or number % n:
                return
        return number
