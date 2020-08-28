"""
    Given a function rand7 which generates a uniform random integer in the 
    range 1 to 7, write a function rand10 which generates a uniform random 
    integer in the range 1 to 10.

    Do NOT use system's Math.random().

    Example:
    Input: 1
    Output: [7]

    Example:
    Input: 2
    Output: [8,4]

    Example:
    Input: 3
    Output: [8,1,10]

    Note:
        1. rand7 is predefined.
        2. Each testcase has one argument: n, the number of times that rand10 
           is called.

    Follow up:
        1. What is the expected value for the number of calls to rand7() 
           function?
        2. Could you minimize the number of calls to rand7()?
"""
#Difficulty: Medium
#10 / 10 test cases passed.
#Runtime: 2312 ms
#Memory Usage: 16.5 MB

#Runtime: 2312 ms, faster than 5.17% of Python3 online submissions for Implement Rand10() Using Rand7().
#Memory Usage: 16.5 MB, less than 78.31% of Python3 online submissions for Implement Rand10() Using Rand7().

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:

    def __init__(self):
        self.count = 0
        self.numbers = {}

    def rand10(self):
        """
        :rtype: int
        """
        while True:
            number = (rand7() * rand7()) ** rand7()
            if number % 10 == 0:
                number = 10
            else:
                number %= 10
            if number not in self.numbers:
                self.numbers[number] = 0
            elif self.numbers[number] <= self.count * 0.10:
                self.count += 1
                self.numbers[number] += 1
                return number
