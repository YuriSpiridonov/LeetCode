"""
    Given an integer array of size n, find all elements that appear more than 
    [ n/3 ] times.

    Note: The algorithm should run in linear time and in O(1) space.

    Example:
    Input: [3,2,3]
    Output: [3]

    Example:
    Input: [1,1,1,3,3,2,2,2]
    Output: [1,2]
"""
#Difficulty: Medium
#66 / 66 test cases passed.
#Runtime: 228 ms
#Memory Usage: 14.8 MB

#Runtime: 228 ms, faster than 7.70% of Python3 online submissions for Majority Element II.
#Memory Usage: 14.8 MB, less than 94.74% of Python3 online submissions for Majority Element II.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        return [num for num in counter if counter[num] > len(nums)/3]
