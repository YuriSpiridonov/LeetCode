"""
    Given an integer array arr, return true if there are three consecutive odd 
    numbers in the array. Otherwise, return false.

    Example:
    Input: arr = [2,6,4,1]
    Output: false
    Explanation: There are no three consecutive odds.

    Example:
    Input: arr = [1,2,34,3,4,5,7,23,12]
    Output: true
    Explanation: [5,7,23] are three consecutive odds.

    Constraints:
        - 1 <= arr.length <= 1000
        - 1 <= arr[i] <= 1000
"""
#Difficulty: Easy
#32 / 32 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14.1 MB

#Runtime: 40 ms, faster than 92.21% of Python3 online submissions for Three Consecutive Odds.
#Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Three Consecutive Odds.

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            if num % 2:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False
