"""
    You are given an integer n. An array nums of length n + 1 is generated in 
    the following way:
        - nums[0] = 0
        - nums[1] = 1
        - nums[2 * i] = nums[i] when 2 <= 2 * i <= n
        - nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

    Return the maximum integer in the array nums​​​.

    Example:
    Input: n = 7
    Output: 3
    Explanation: According to the given rules:
                   nums[0] = 0
                   nums[1] = 1
                   nums[(1 * 2) = 2] = nums[1] = 1
                   nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
                   nums[(2 * 2) = 4] = nums[2] = 1
                   nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
                   nums[(3 * 2) = 6] = nums[3] = 2
                   nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
                 Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.

    Example:
    Input: n = 2
    Output: 1
    Explanation: According to the given rules, the maximum between nums[0], 
                 nums[1], and nums[2] is 1.

    Example:
    Input: n = 3
    Output: 2
    Explanation: According to the given rules, the maximum between nums[0], 
                 nums[1], nums[2], and nums[3] is 2.

    Constraints:
        - 0 <= n <= 100
"""
#Difficulty: Easy
#101 / 101 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.1 MB

#Runtime: 32 ms, faster than 68.40% of Python3 online submissions for Get Maximum in Generated Array.
#Memory Usage: 14.1 MB, less than 82.45% of Python3 online submissions for Get Maximum in Generated Array.

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        arr = [0, 1] + [None] * (n-1)
        i = 1
        while None in arr:
            arr[2*i] = arr[i]
            if 2*i + 1 <= n:
                arr[2*i + 1] = arr[i] + arr[i+1]
            i += 1
        return max(arr)
