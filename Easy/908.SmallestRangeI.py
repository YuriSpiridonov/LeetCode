'''
    Given an array A of integers, for each integer A[i] we 
    may choose any x with -K <= x <= K, and add x to A[i].

    After this process, we have some array B.

    Return the smallest possible difference between the 
    maximum value of B and the minimum value of B.

    Example:
    Input: A = [1], K = 0
    Output: 0
    Explanation: B = [1]

    Example:
    Input: A = [0,10], K = 2
    Output: 6
    Explanation: B = [2,8]

    Example:
    Input: A = [1,3,6], K = 3
    Output: 0
    Explanation: B = [3,3,3] or B = [4,4,4]

    Note:
        1. 1 <= A.length <= 10000
        2. 0 <= A[i] <= 10000
        3. 0 <= K <= 10000
'''
#Difficulty: Easy
#68 / 68 test cases passed.
#Runtime: 128 ms
#Memory Usage: 15.2 MB

#Runtime: 112 ms, faster than 57.39% of Python3 online submissions for Smallest Range I.
#Memory Usage: 15.2 MB, less than 82.08% of Python3 online submissions for Smallest Range I.

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        A.sort()
        if A[0] + K >= A[-1] - K:
            return 0
        return A[-1] - A[0] - K*2
