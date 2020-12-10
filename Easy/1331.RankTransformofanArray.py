'''
    Given an array of integers arr, replace each element with its rank.

    The rank represents how large the element is. The rank has the 
    following rules:
        - Rank is an integer starting from 1.
        - The larger the element, the larger the rank. If two elements 
          are equal, their rank must be the same.
        - Rank should be as small as possible.

    Example:
    Input: arr = [40,10,20,30]
    Output: [4,1,2,3]
    Explanation: 40 is the largest element. 10 is the smallest. 20 is 
                 the second smallest. 30 is the third smallest.

    Example:
    Input: arr = [100,100,100]
    Output: [1,1,1]
    Explanation: Same elements share the same rank.

    Example:
    Input: arr = [37,12,28,9,100,56,80,5,12]
    Output: [5,3,4,2,8,6,7,1,3]

    Constraints:
        - 0 <= arr.length <= 10^5
        - -10^9 <= arr[i] <= 10^9
'''
#Difficulty: Easy
#37 / 37 test cases passed.
#Runtime: 340 ms
#emory Usage: 36.2 MB

#Runtime: 340 ms, faster than 66.17% of Python3 online submissions for Rank Transform of an Array.
#Memory Usage: 36.2 MB, less than 19.18% of Python3 online submissions for Rank Transform of an Array.

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums_indices = {}
        sorted_array = sorted(set(arr))
        for index, num in enumerate(sorted_array):
            nums_indices[num] = index
        for index, num in enumerate(arr):
            arr[index] = 1 + nums_indices[num]
        return arr
