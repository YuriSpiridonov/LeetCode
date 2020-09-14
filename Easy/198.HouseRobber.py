"""
    You are a professional robber planning to rob houses along a street. Each 
    house has a certain amount of money stashed, the only constraint stopping 
    you from robbing each of them is that adjacent houses have security system 
    connected and it will automatically contact the police if two adjacent 
    houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of 
    each house, determine the maximum amount of money you can rob tonight 
    without alerting the police.

    Example:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                 Total amount you can rob = 1 + 3 = 4.

    Example:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and 
                 rob house 5 (money = 1).
                 Total amount you can rob = 2 + 9 + 1 = 12.

    Constraints:
        - 0 <= nums.length <= 100
        - 0 <= nums[i] <= 400
"""
#Difficulty: Easy
#69 / 69 test cases passed.
#Runtime: 40 ms
#Memory Usage: 13.8 MB

#Runtime: 40 ms, faster than 27.94% of Python3 online submissions for House Robber.
#Memory Usage: 13.8 MB, less than 69.22% of Python3 online submissions for House Robber.

class Solution:
    def rob(self, nums: List[int]) -> int:
        odd_num = 0
        even_num = 0
        for i in range(len(nums)):
            if i % 2:
                odd_num += nums[i]
                odd_num = max(odd_num, even_num)
            else:
                even_num += nums[i]
                even_num = max(odd_num, even_num)
        return max(odd_num, even_num)
