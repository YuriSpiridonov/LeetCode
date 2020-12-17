'''
    Given an array of distinct integers arr, find all pairs 
    of elements with the minimum absolute difference of any 
    two elements. 

    Return a list of pairs in ascending order(with respect 
    to pairs), each pair [a, b] follows
        - a, b are from arr
        - a < b
        - b - a equals to the minimum absolute difference 
          of any two elements in arr

    Example:
    Input: arr = [4,2,1,3]
    Output: [[1,2],[2,3],[3,4]]
    Explanation: The minimum absolute difference is 1. List 
                 all pairs with difference equal to 1 in 
                 ascending order.

    Example:
    Input: arr = [1,3,6,10,15]
    Output: [[1,3]]

    Example:
    Input: arr = [3,8,-10,23,19,-4,-14,27]
    Output: [[-14,-10],[19,23],[23,27]]

    Constraints:
        - 2 <= arr.length <= 10^5
        - -10^6 <= arr[i] <= 10^6
'''
#Difficulty: Easy
#36 / 36 test cases passed.
#Runtime: 428 ms
#Memory Usage: 35.3 MB

#Runtime: 428 ms, faster than 10.53% of Python3 online submissions for Minimum Absolute Difference.
#Memory Usage: 35.3 MB, less than 5.95% of Python3 online submissions for Minimum Absolute Difference.

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        difference = {}
        min_diff = float(inf)
        for i in range(1, len(arr)):
            value = abs(arr[i-1] - arr[i])
            min_diff = min(min_diff, value)
            if value not in difference:
                difference[value] = []
            difference[value].append([arr[i-1], arr[i]])
        return difference[min_diff]
