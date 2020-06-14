"""
    Given a sorted array arr, two integers k and x, find the k closest elements 
    to x in the array. The result should also be sorted in ascending order. 
    If there is a tie, the smaller elements are always preferred.

    Example:
    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]
    
    Constraints:
        - 1 <= k <= arr.length
        - 1 <= arr.length <= 10^4
        - Absolute value of elements in the array and x will not exceed 104
"""
#Difficulty: Medium
#59 / 59 test cases passed.
#Runtime: 320 ms
#Memory Usage: 15.3 MB

#Runtime: 320 ms, faster than 70.14% of Python3 online submissions for Find K Closest Elements.
#Memory Usage: 15.3 MB, less than 41.69% of Python3 online submissions for Find K Closest Elements.

class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        length = len(arr)
        l = 0
        r = length - 1
        while l + 1 < r:
            m = (l + r) // 2
            if arr[m-1] <= x <= arr[m]:
                l, r = self.pickNumber(arr, m, k, x, length)
                return arr[l: r+1]
            if x < arr[m]:
                r = m
            else:
                l = m
        if l == 0:
            return arr[:min(k, length)]
        if r == length - 1:
            return arr[-k:]

    def pickNumber(self, arr, m, k, x, length):
        result = []
        i = 1
        j = 0
        while k > 0:
            if m + j > length - 1:
                result.sort()
                return result[0] - k, result[-1]
            if m-i >= 0 and x - arr[m-i] <= arr[m + j] - x:
                result.append(m-i)
                i += 1
            else:
                result.append(m + j)
                j += 1
            k -= 1
        result.sort()
        return result[0], result[-1]
