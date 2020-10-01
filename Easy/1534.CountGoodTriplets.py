"""
    Given an array of integers arr, and three integers a, b and c. You need to 
    find the number of good triplets.
    A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are 
    true:
        - 0 <= i < j < k < arr.length
        - |arr[i] - arr[j]| <= a
        - |arr[j] - arr[k]| <= b
        - |arr[i] - arr[k]| <= c

    Where |x| denotes the absolute value of x.
    Return the number of good triplets.

    Example:
    Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
    Output: 4
    Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

    Example:
    Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
    Output: 0
    Explanation: No triplet satisfies all conditions.

    Constraints:
        - 3 <= arr.length <= 100
        - 0 <= arr[i] <= 1000
        - 0 <= a, b, c <= 1000
"""
#Difficulty: Easy
#92 / 92 test cases passed.
#Runtime: 328 ms
#Memory Usage: 14.2 MB

#Runtime: 328 ms, faster than 97.91% of Python3 online submissions for Count Good Triplets.
#Memory Usage: 14.2 MB, less than 10.62% of Python3 online submissions for Count Good Triplets.

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        count = 0
        for i in range(length):
            for j in range(i+1, length):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, length):
                        if abs(arr[i] - arr[k]) <= c and abs(arr[j] - arr[k]) <= b:
                            count += 1
        return count
