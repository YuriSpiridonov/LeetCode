'''
    Given an array nums of n integers, are there elements 
    a, b, c in nums such that a + b + c = 0? Find all unique 
    triplets in the array which gives the sum of zero.

    Notice that the solution set must not contain duplicate 
    triplets.

    Example:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Example:
    Input: nums = []
    Output: []

    Example:
    Input: nums = [0]
    Output: []

    Constraints:
        - 0 <= nums.length <= 3000
        - -10^5 <= nums[i] <= 10^5
'''
#Difficulty: Medium
#318 / 318 test cases passed.
#Runtime: 5752 ms
#Memory Usage: 17.4 MB

#Runtime: 5752 ms, faster than 5.04% of Python3 online submissions for 3Sum.
#Memory Usage: 17.4 MB, less than 50.85% of Python3 online submissions for 3Sum.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        if not nums or length < 3:
            return result 
        nums.sort()
        for i in range(length):
            j = i + 1
            k = length - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k] 
                if s == 0 and [nums[i], nums[j], nums[k]] not in result:
                    result.append([nums[i], nums[j], nums[k]])
                    prev = nums[j]
                    while nums[j] == prev and j < k:
                        j += 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return result
