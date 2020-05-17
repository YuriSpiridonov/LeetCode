"""
    Given an array arr, replace every element in that array with the greatest 
    element among the elements to its right, and replace the last element with -1.
    After doing so, return the array.

    Example:
    Input: arr = [17,18,5,4,6,1]
    Output: [18,6,6,6,1,-1]
"""
#Difficulty: Easy
#15 / 15 test cases passed.
#Runtime: 112 ms
#Memory Usage: 14.8 MB

#Runtime: 112 ms, faster than 99.50% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
#Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-1
        greater = -1
        while i >= 0:
            if arr[i] > greater:
                arr[i], greater =  greater, arr[i]
            else:
                arr[i] = greater
            i -= 1
        return arr
