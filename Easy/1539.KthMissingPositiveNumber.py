"""
    Given an array arr of positive integers sorted in a strictly increasing 
    order, and an integer k.
    Find the kth positive integer that is missing from this array.

    Example:
    Input: arr = [2,3,4,7,11], k = 5
    Output: 9
    Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
                 The 5th missing positive integer is 9.

    Example:
    Input: arr = [1,2,3,4], k = 2
    Output: 6
    Explanation: The missing positive integers are [5,6,7,...]. 
                 The 2nd missing positive integer is 6.

    Constraints:
        - 1 <= arr.length <= 1000
        - 1 <= arr[i] <= 1000
        - 1 <= k <= 1000
        - arr[i] < arr[j] for 1 <= i < j <= arr.length
"""
#Difficulty: Easy
#83 / 83 test cases passed.
#Runtime: 52 ms
#Memory Usage: 13.8 MB

#Runtime: 52 ms, faster than 82.94% of Python3 online submissions for Kth Missing Positive Number.
#Memory Usage: 13.8 MB, less than 92.67% of Python3 online submissions for Kth Missing Positive Number.

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        maximum = max(arr)
        array = [0] * 1001
        for number in arr:
            array[number] = number
        for i in range(1, maximum):
            if not array[i]:
                k -= 1
            if k == 0:
                return i
        return maximum + k
