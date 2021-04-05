'''
    We have some permutation A of [0, 1, ..., N - 1], where 
    N is the length of A.

    The number of (global) inversions is the number of i < j 
    with 0 <= i < j < N and A[i] > A[j].

    The number of local inversions is the number of i with 
    0 <= i < N and A[i] > A[i+1].

    Return true if and only if the number of global inversions 
    is equal to the number of local inversions.

    Example:
    Input: A = [1,0,2]
    Output: true
    Explanation: There is 1 global inversion, and 1 local 
                 inversion.

    Example:
    Input: A = [1,2,0]
    Output: false
    Explanation: There are 2 global inversions, and 1 local 
                 inversion.

    Note:
        - A will be a permutation of [0, 1, ..., A.length - 1].
        - A will have length in range [1, 5000].
        - The time limit for this problem has been reduced.
'''
#Difficulty: Medium
#

#Runtime: 324 ms, faster than 86.59% of Python3 online submissions for Global and Local Inversions.
#Memory Usage: 15.1 MB, less than 44.06% of Python3 online submissions for Global and Local Inversions.

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True