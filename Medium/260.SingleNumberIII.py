'''
    Given an integer array nums, in which exactly two elements 
    appear only once and all the other elements appear exactly 
    twice. Find the two elements that appear only once. You can 
    return the answer in any order.

    Follow up: Your algorithm should run in linear runtime 
    complexity. Could you implement it using only constant 
    space complexity?

    Example:
    Input: nums = [1,2,1,3,2,5]
    Output: [3,5]
    Explanation:  [5, 3] is also a valid answer.

    Example:
    Input: nums = [-1,0]
    Output: [-1,0]

    Example:
    Input: nums = [0,1]
    Output: [1,0]

    Constraints:
        - 2 <= nums.length <= 3 * 10^4
        - -2^31 <= nums[i] <= 2^31 - 1
        - Each integer in nums will appear twice, only two 
          integers will appear once.
'''
#Difficulty: Medium
#32 / 32 test cases passed.
#Runtime: 56 ms
#Memory Usage: 16.2 MB

#Runtime: 56 ms, faster than 82.01% of Python3 online submissions for Single Number III.
#Memory Usage: 16.2 MB, less than 21.37% of Python3 online submissions for Single Number III.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        single = set()
        for num in nums:
            if num not in single:
                single.add(num)
            else:
                single.remove(num)
        return single
