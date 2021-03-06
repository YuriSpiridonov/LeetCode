'''
    Given four lists A, B, C, D of integer values, compute 
    how many tuples (i, j, k, l) there are such that 
    A[i] + B[j] + C[k] + D[l] is zero.

    To make problem a bit easier, all A, B, C, D have same 
    length of N where 0 ≤ N ≤ 500. All integers are in the 
    range of -228 to 228 - 1 and the result is guaranteed 
    to be at most 231 - 1.

    Example:
    Input:
            A = [ 1, 2]
            B = [-2,-1]
            C = [-1, 2]
            D = [ 0, 2]
    Output:
            2
    Explanation:
            The two tuples are:
            1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 
            1 + (-2) + (-1) + 2 = 0
            2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 
            2 + (-1) + (-1) + 0 = 0
'''
#Difficulty: Medium
#48 / 48 test cases passed.
#Runtime: 268 ms
#Memory Usage: 35.2 MB

#Runtime: 268 ms, faster than 75.51% of Python3 online submissions for 4Sum II.
#Memory Usage: 35.2 MB, less than 49.47% of Python3 online submissions for 4Sum II.

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        result = 0
        absum = {}
        for a in A:
            for b in B:
                n = a + b
                if n not in absum:
                    absum[n] = 0
                absum[n] += 1
        for c in C:
            for d in D:
                m = -c - d
                if m in absum:
                    result += absum[m]
        return result
