"""
    Write a program that outputs the string representation of numbers from 1 
    to n.
    But for multiples of three it should output “Fizz” instead of the number 
    and for the multiples of five output “Buzz”. For numbers which are 
    multiples of both three and five output “FizzBuzz”.

    Example:
    n = 15,
    Return:
    [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
"""
#Difficulty: Easy
#8 / 8 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14.7 MB

#Runtime: 40 ms, faster than 88.30% of Python3 online submissions for Fizz Buzz.
#Memory Usage: 14.7 MB, less than 96.17% of Python3 online submissions for Fizz Buzz.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        result = []
        while i <= n:
            if not i % 3 and not i % 5:
                result.append('FizzBuzz')
            elif not i % 5:
                result.append('Buzz')
            elif not i % 3:
                result.append('Fizz')
            else:
                result.append(str(i))
            i += 1
        return result
