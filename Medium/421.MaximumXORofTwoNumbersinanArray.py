"""
    Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
    Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
    Could you do this in O(n) runtime?

    Example:
    Input: [3, 10, 5, 25, 2, 8]
    Output: 28
    Explanation: The maximum result is 5 ^ 25 = 28.
"""
#Difficulty: Medium
#29 / 29 test cases passed.
#Runtime: 188 ms
#Memory Usage: 18 MB

#Runtime: 188 ms, faster than 72.25% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
#Memory Usage: 18 MB, less than 89.19% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maximum = 0
        mask = 0
        result = set()
        length = len(nums)
        for i in range(30, -1, -1):
            mask |= 1 << i
            new = maximum | 1 << i
            for i in range(length):
                result.add(nums[i] & mask)
            for prefix in result:
                if new ^ prefix  in result:
                    maximum = new
                    break
            result.clear()
        return maximum
