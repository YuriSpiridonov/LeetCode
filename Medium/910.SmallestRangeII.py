'''
    Given an array A of integers, for each integer A[i] we 
    need to choose either x = -K or x = K, and add x to A[i] 
    (only once).

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
    Output: 3
    Explanation: B = [4,6,3]

    Note:
        1. 1 <= A.length <= 10000
        2. 0 <= A[i] <= 10000
        3. 0 <= K <= 10000
'''
#Difficulty: Medium
#68 / 68 test cases passed.
#Runtime: 132 ms
#Memory Usage: 16.1 MB

#Runtime: 132 ms, faster than 100.00% of Python3 online submissions for Smallest Range II.
#Memory Usage: 16.1 MB, less than 6.47% of Python3 online submissions for Smallest Range II.

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A = list(set(A))
        A.sort()
        minimum = A[0]
        maximum = A[-1]
        result = maximum - minimum
        if result < K:
            return result
        for i in range(len(A)-1):
            lo = min(minimum + K, A[i+1] - K)
            hi = max(maximum - K, A[i] + K)
            result = min(result, hi - lo)
        return result
