'''
    For a non-negative integer X, the array-form of X is an 
    array of its digits in left to right order.  For example, 
    if X = 1231, then the array form is [1,2,3,1].

    Given the array-form A of a non-negative integer X, 
    return the array-form of the integer X+K.

    Example:
    Input: A = [1,2,0,0], K = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234

    Example:
    Input: A = [2,7,4], K = 181
    Output: [4,5,5]
    Explanation: 274 + 181 = 455

    Example:
    Input: A = [2,1,5], K = 806
    Output: [1,0,2,1]
    Explanation: 215 + 806 = 1021

    Example:
    Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
    Output: [1,0,0,0,0,0,0,0,0,0,0]
    Explanation: 9999999999 + 1 = 10000000000

    Note：
        1. 1 <= A.length <= 10000
        2. 0 <= A[i] <= 9
        3. 0 <= K <= 10000
        4. If A.length > 1, then A[0] != 0
'''
#Difficulty: Easy
#156 / 156 test cases passed.
#Runtime: 796 ms
#Memory Usage: 15 MB

#Runtime: 796 ms, faster than 11.63% of Python3 online submissions for Add to Array-Form of Integer.
#Memory Usage: 15 MB, less than 70.03% of Python3 online submissions for Add to Array-Form of Integer.

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        n = 0
        for a in A:
            n = n*10 + a
        n += K
        A = []
        while n > 0:
            A.append(n%10)
            n //= 10
        return A[::-1] if A else [0]
