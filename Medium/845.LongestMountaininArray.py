"""
    Let's call any (contiguous) subarray B (of A) a mountain if the following 
    properties hold:

        - B.length >= 3
        - There exists some 0 < i < B.length - 1 such that 
          B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
    (Note that B could be any subarray of A, including the entire array A.)

    Given an array A of integers, return the length of the longest mountain. 

    Return 0 if there is no mountain.

    Example:
    Input: [2,1,4,7,3,2,5]
    Output: 5
    Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

    Example:
    Input: [2,2,2]
    Output: 0
    Explanation: There is no mountain.

    Note:
        1. 0 <= A.length <= 10000
        2. 0 <= A[i] <= 10000

    Follow up:
        - Can you solve it using only one pass?
        - Can you solve it in O(1) space?
"""
#Difficulty: 
#72 / 72 test cases passed.
#Runtime: 152 ms
#Memory Usage: 15.2 MB

#Runtime: 152 ms, faster than 97.47% of Python3 online submissions for Longest Mountain in Array.
#Memory Usage: 15.2 MB, less than 11.66% of Python3 online submissions for Longest Mountain in Array.

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0
        prev = A[0]
        count = 1
        result = 0
        flag = True
        for n in A[1:]:
            if n > prev and flag:
                prev = n
                count += 1
            elif n > prev and not flag:
                prev = n
                count = 2
                flag = True
                result = max(result, count)
            elif count >= 2 and n < prev:
                prev = n
                count += 1
                flag = False
                result = max(result, count)
            else:
                prev = n
                count = 1
        return result if result >= 3 else 0
