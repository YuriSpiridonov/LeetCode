"""
    Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all 
    elements in arr2 are also in arr1.
    Sort the elements of arr1 such that the relative ordering of items in arr1 
    are the same as in arr2.  Elements that don't appear in arr2 should be 
    placed at the end of arr1 in ascending order.

    Example:
    Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
    Output: [2,2,2,1,4,3,3,9,6,7,19]

    Constraints:
        - arr1.length, arr2.length <= 1000
        - 0 <= arr1[i], arr2[i] <= 1000
        - Each arr2[i] is distinct.
        - Each arr2[i] is in arr1.
"""
#Difficulty: Easy
#16 / 16 test cases passed.
#Runtime: 48 ms
#Memory Usage: 13.9 MB    

#Runtime: 48 ms, faster than 51.84% of Python3 online submissions for Relative Sort Array.
#Memory Usage: 13.9 MB, less than 67.55% of Python3 online submissions for Relative Sort Array.   

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        head = []
        tail = []
        diff = list(set(arr1).difference(set(arr2)))
        for num in arr2:
            head.extend([num] * arr1.count(num))
        for num in diff:
            tail.extend([num] * arr1.count(num))
        return head + sorted(tail)
