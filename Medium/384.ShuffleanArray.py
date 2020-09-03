"""
    Shuffle a set of numbers without duplicates.

    Example:
        // Init an array with set 1, 2, and 3.
        int[] nums = {1,2,3};
        Solution solution = new Solution(nums);

        // Shuffle the array [1,2,3] and return its result. Any permutation of 
        // [1,2,3] must equally likely to be returned.
        solution.shuffle();

        // Resets the array back to its original configuration [1,2,3].
        solution.reset();

        // Returns the random shuffling of array [1,2,3].
        solution.shuffle();
"""
#Difficulty: Medium
#10 / 10 test cases passed.
#Runtime: 304 ms
#Memory Usage: 18.7 MB

#Runtime: 304 ms, faster than 86.33% of Python3 online submissions for Shuffle an Array.
#Memory Usage: 18.7 MB, less than 97.99% of Python3 online submissions for Shuffle an Array.

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return random.sample(self.nums, len(self.nums))


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
