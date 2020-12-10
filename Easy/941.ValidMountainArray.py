'''
    Given an array of integers arr, return true if and only if it is a 
    valid mountain array.

    Recall that arr is a mountain array if and only if:
        - arr.length >= 3
        - There exists some i with 0 < i < arr.length - 1 such that:
            =  arr[0] < arr[1] < ... < arr[i - 1] < A[i]
            =  arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

    Example:
    Input: arr = [2,1]
    Output: false

    Example:
    Input: arr = [3,5,5]
    Output: false

    Example:
    Input: arr = [0,3,2,1]
    Output: true

    Constraints:
        - 1 <= arr.length <= 10^4
        - 0 <= arr[i] <= 10^4
'''
#Difficulty: Easy
#52 / 52 test cases passed.
#Runtime: 188 ms
#Memory Usage: 15.6 MB

#Runtime: 188 ms, faster than 93.89% of Python3 online submissions for Valid Mountain Array.
#Memory Usage: 15.6 MB, less than 16.18% of Python3 online submissions for Valid Mountain Array.

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        prev = arr[0]
        left = False
        top = False
        for nxt in arr[1:]:
            if not top and prev < nxt:
                left = True
            elif prev > nxt:
                top = True
            else:
                return False
            prev = nxt
        return left and top
