"""
    Given an array A of non-negative integers, return an array consisting of 
    all the even elements of A, followed by all the odd elements of A.

    You may return any answer array that satisfies this condition.

    Example:
    Input: [3,1,2,4]
    Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

    Note:
    1 <= A.length <= 5000
    0 <= A[i] <= 5000
"""
#Difficulty: Easy
#285 / 285 test cases passed.
#Runtime: 76 ms
#Memory Usage: 14.2 MB

#Runtime: 76 ms, faster than 91.94% of Python3 online submissions for Sort Array By Parity.
#Memory Usage: 14.2 MB, less than 5.19% of Python3 online submissions for Sort Array By Parity.

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = list()
        odd = list()
        for n in A:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        return even + odd
