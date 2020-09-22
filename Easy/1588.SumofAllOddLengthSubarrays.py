"""
    Given an array of positive integers arr, calculate the sum of all possible 
    odd-length subarrays.
    A subarray is a contiguous subsequence of the array.
    Return the sum of all odd-length subarrays of arr.

    Example:
    Input: arr = [1,4,2,5,3]
    Output: 58
    Explanation: The odd-length subarrays of arr and their sums are:
                 [1] = 1
                 [4] = 4
                 [2] = 2
                 [5] = 5
                 [3] = 3
                 [1,4,2] = 7
                 [4,2,5] = 11
                 [2,5,3] = 10
                 [1,4,2,5,3] = 15
                 If we add all these together we get 
                                     1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

    Example:
    Input: arr = [1,2]
    Output: 3
    Explanation: There are only 2 subarrays of odd length, [1] and [2]. 
                 Their sum is 3.

    Example:
    Input: arr = [10,11,12]
    Output: 66

    Constraints:
        - 1 <= arr.length <= 100
        - 1 <= arr[i] <= 1000
"""
#Difficulty: Easy
#96 / 96 test cases passed.
#Runtime: 72 ms
#Memory Usage: 13.7 MB

#Runtime: 72 ms, faster than 55.77% of Python3 online submissions for Sum of All Odd Length Subarrays.
#Memory Usage: 13.7 MB, less than 93.54% of Python3 online submissions for Sum of All Odd Length Subarrays.

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i, j = 0, 3
        result = sum(arr)
        length = len(arr)
        while j <= length:
            result += sum(arr[i:i+j])
            i += 1
            if i + j > length:
                i = 0
                j += 2
        return result
