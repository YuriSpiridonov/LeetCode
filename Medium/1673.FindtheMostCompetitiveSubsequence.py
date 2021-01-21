"""
    Given an integer array nums and a positive integer k, 
    return the most competitive subsequence of nums of size 
    k.

    An array's subsequence is a resulting sequence obtained 
    by erasing some (possibly zero) elements from the array.

    We define that a subsequence a is more competitive than 
    a subsequence b (of the same length) if in the first 
    position where a and b differ, subsequence a has a 
    number less than the corresponding number in b. For 
    example, [1,3,4] is more competitive than [1,3,5] 
    because the first position they differ is at the final 
    number, and 4 is less than 5.

    Example:
    Input: nums = [3,5,2,6], k = 2
    Output: [2,6]
    Explanation: Among the set of every possible subsequence: 
                 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, 
                 [2,6] is the most competitive.

    Example:
    Input: nums = [2,4,3,3,5,4,9,6], k = 4
    Output: [2,3,3,4]

    Constraints:
        - 1 <= nums.length <= 10^5
        - 0 <= nums[i] <= 10^9
        - 1 <= k <= nums.length
"""
#Difficulty: Medium
#86 / 86 test cases passed.
#Runtime: 1256 ms
#Memory Usage: 27.1 MB

#Runtime: 1256 ms, faster than 78.12% of Python3 online submissions for Find the Most Competitive Subsequence.
#Memory Usage: 27.1 MB, less than 81.07% of Python3 online submissions for Find the Most Competitive Subsequence.

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        length = len(nums) - k
        stack = []
        for num in nums:
            while stack and stack[-1] > num and length:
                stack.pop()
                length -= 1
            stack.append(num)
        return stack[:k]