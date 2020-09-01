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
#Runtime: 7548 ms
#Memory Usage: 15.7 MB

#Runtime: 7548 ms, faster than 5.06% of Python3 online submissions for N-Repeated Element in Size 2N Array.
#Memory Usage: 15.7 MB, less than 5.01% of Python3 online submissions for N-Repeated Element in Size 2N Array.

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A) // 2
        digits = set(A)
        for digit in digits:
            if A.count(digit) == N:
                return digit
