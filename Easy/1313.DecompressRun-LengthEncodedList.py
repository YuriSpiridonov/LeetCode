"""
    We are given a list nums of integers representing a list compressed with
    run-length encoding.
    Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] 
    (with i >= 0).  For each such pair, there are freq elements with value val 
    concatenated in a sublist. Concatenate all the sublists from left to right 
    to generate the decompressed list.
    Return the decompressed list.

    Example:
    Input: nums = [1,2,3,4]
    Output: [2,4,4,4]
    Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we 
                 generate the array [2].
                 The second pair [3,4] means we have freq = 3 and val = 4 so we 
                 generate [4,4,4].
                 At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

    Constraints:
        - 2 <= nums.length <= 100
        - nums.length % 2 == 0
        - 1 <= nums[i] <= 100
"""
#Difficulty: Easy
#53 / 53 test cases passed.
#Runtime: 64 ms
#Memory Usage: 13.9 MB

#Runtime: 64 ms, faster than 92.84% of Python3 online submissions for Decompress Run-Length Encoded List.
#Memory Usage: 13.9 MB, less than 82.98% of Python3 online submissions for Decompress Run-Length Encoded List.

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 1
        length = len(nums)
        result = []
        while i < length:
            result += [nums[i]] * nums[i-1]
            i += 2
        return result
