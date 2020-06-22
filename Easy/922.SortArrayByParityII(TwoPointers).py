"""
    Given an array A of non-negative integers, half of the integers in A are 
    odd, and half of the integers are even.
    Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] 
    is even, i is even.
    You may return any answer array that satisfies this condition.

    Example:
    Input: [4,2,5,7]
    Output: [4,5,2,7]
    Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

    Note:
        1. 2 <= A.length <= 20000
        2. A.length % 2 == 0
        3. 0 <= A[i] <= 1000
"""
#Difficulty: Easy
#61 / 61 test cases passed.
#Runtime: 204 ms
#Memory Usage: 16 MB
        
#Runtime: 204 ms, faster than 99.17% of Python3 online submissions for Sort Array By Parity II.
#Memory Usage: 16 MB, less than 98.98% of Python3 online submissions for Sort Array By Parity II.
        
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        l = len(A)
        j = 1
        for i in range(0, l, 2):
            if A[i] % 2:
                    while A[j] % 2:
                        j += 2
                    A[i], A[j] = A[j], A[i]
        return A
