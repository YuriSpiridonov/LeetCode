"""
    In a array A of size 2N, there are N+1 unique elements, and exactly one of 
    these elements is repeated N times.

    Return the element repeated N times.

    Example:
    Input: [1,2,3,3]
    Output: 3

    Example:
    Input: [2,1,2,5,3,2]
    Output: 2

    Example:
    Input: [5,1,5,2,5,3,5,4]
    Output: 5

    Note:
        - 4 <= A.length <= 10000
        - 0 <= A[i] < 10000
        - A.length is even
"""
#Difficulty: Easy
#102 / 102 test cases passed.
#Runtime: 320 ms
#Memory Usage: 15.2 MB

#Runtime: 320 ms, faster than 27.67% of Python3 online submissions for N-Repeated Element in Size 2N Array.
#Memory Usage: 15.2 MB, less than 22.20% of Python3 online submissions for N-Repeated Element in Size 2N Array.

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        digits = {}
        for d in A:
            if d not in digits:
                digits[d] = 0
            digits[d] += 1
        return max(digits, key=digits.get)
