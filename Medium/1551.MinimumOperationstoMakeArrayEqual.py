'''
    You have an array arr of length n where arr[i] = (2 * i) + 1 
    for all valid values of i (i.e. 0 <= i < n).

    In one operation, you can select two indices x and y 
    where 0 <= x, y < n and subtract 1 from arr[x] and add 
    1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). 
    The goal is to make all the elements of the array equal. 
    It is guaranteed that all the elements of the array can 
    be made equal using some operations.

    Given an integer n, the length of the array. Return the 
    minimum number of operations needed to make all the 
    elements of arr equal.

    Example:
    Input: n = 3
    Output: 2
    Explanation: arr = [1, 3, 5]
                 First operation choose x = 2 and y = 0, 
                 this leads arr to be [2, 3, 4]
                 In the second operation choose x = 2 and 
                 y = 0 again, thus arr = [3, 3, 3].

    Example:
    Input: n = 6
    Output: 9

    Constraints:

        - 1 <= n <= 10^4
'''
#Difficulty: Medium
#301 / 301 test cases passed.
#Runtime: 76 ms
#Memory Usage: 14.3 MB

#Runtime: 76 ms, faster than 38.50% of Python3 online submissions for Minimum Operations to Make Array Equal.
#Memory Usage: 14.3 MB, less than 50.38% of Python3 online submissions for Minimum Operations to Make Array Equal.

class Solution:
    def minOperations(self, n: int) -> int:
        x = (2 + 2*(n-1)) // 2
        y = 0
        for i in range(n//2):
            y += x - (i*2+1)
        return y