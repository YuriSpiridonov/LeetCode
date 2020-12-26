'''
    Given an array nums of 0s and 1s and an integer k, 
    return True if all 1's are at least k places away from 
    each other, otherwise return False.

    Example:
    Input: nums = [1,0,0,0,1,0,0,1], k = 2
    Output: true
    Explanation: Each of the 1s are at least 2 places away 
                 from each other.

    Example:
    Input: nums = [1,0,0,1,0,1], k = 2
    Output: false
    Explanation: The second 1 and third 1 are only one apart 
                 from each other.

    Example:
    Input: nums = [1,1,1,1,1], k = 0
    Output: true

    Example:
    Input: nums = [0,1,0,1], k = 1
    Output: true

    Constraints:
        - 1 <= nums.length <= 10^5
        - 0 <= k <= nums.length
        - nums[i] is 0 or 1
'''
#Difficulty: Medium
#66 / 66 test cases passed.
#Runtime: 552 ms
#Memory Usage: 17.8 MB

#Runtime: 552 ms, faster than 73.70% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
#Memory Usage: 17.8 MB, less than 15.89% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums:
            return True
        nums = nums[nums.index(1):]
        nums = nums[::-1]
        nums = nums[nums.index(1):]
        count = 0
        result = []
        for num in nums:
            if num == 0:
                count += 1
            else:
                result.append(count)
                count = 0
        return min(result[1:]) >= k if result[1:] else result
