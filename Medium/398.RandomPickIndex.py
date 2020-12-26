'''
    Given an array of integers with possible duplicates, 
    randomly output the index of a given target number. 
    You can assume that the given target number must exist 
    in the array.

    Note:
    The array size can be very large. Solution that uses too 
    uch extra space will not pass the judge.

    Example:

    int[] nums = new int[] {1,2,3,3,3};
    Solution solution = new Solution(nums);

    // pick(3) should return either index 2, 3, or 4 randomly. 
    // Each index should have equal probability of returning.
    solution.pick(3);

    // pick(1) should return 0. Since in the array only nums[0] 
    // is equal to 1.
    solution.pick(1);
'''
#Difficulty: Medium
#13 / 13 test cases passed.
#Runtime: 312 ms
#Memory Usage: 23.9 MB

#Runtime: 312 ms, faster than 42.11% of Python3 online submissions for Random Pick Index.
#Memory Usage: 23.9 MB, less than 8.02% of Python3 online submissions for Random Pick Index.

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = {}
        self.index(nums)

    def pick(self, target: int) -> int:
        return random.choice(self.nums[target])
    
    def index(self, nums):
        for index, num in enumerate(nums):
            if num not in self.nums:
                self.nums[num] = []
            self.nums[num].append(index)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
