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
#Runtime: 228 ms
#Memory Usage: 16.5 MB

#Runtime: 228 ms, faster than 54.40% of Python3 online submissions for Sort Array By Parity II.
#Memory Usage: 16.5 MB, less than 11.57% of Python3 online submissions for Sort Array By Parity II.

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        db = {'odd' : [], 'even' : []}
        B = []
        l = len(A)
        for a in A:
            if a % 2:
                db['odd'].append(a)
            else:
                db['even'].append(a)
        for i in range(l // 2):
            B.append(db['even'][i])
            B.append(db['odd'][i])
        return B
