'''
    Given an integer array nums, handle multiple queries of 
    the following types:
        1. Update the value of an element in nums.
        2. Calculate the sum of the elements of nums between 
           indices left and right inclusive where 
           left <= right.

    Implement the NumArray class:
        - NumArray(int[] nums) Initializes the object with 
          the integer array nums.
        - void update(int index, int val) Updates the value 
          of nums[index] to be val.
        - int sumRange(int left, int right) Returns the sum 
          of the elements of nums between indices left and 
          right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

    Example:
    Input
    ["NumArray", "sumRange", "update", "sumRange"]
    [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    Output
    [null, 9, null, 8]

    Explanation
                NumArray numArray = new NumArray([1, 3, 5]);
                numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
                numArray.update(1, 2);   // nums = [1, 2, 5]
                numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

    Constraints:
        - 1 <= nums.length <= 3 * 10^4
        - -100 <= nums[i] <= 100
        - 0 <= index < nums.length
        - -100 <= val <= 100
        - 0 <= left <= right < nums.length
        - At most 3 * 104 calls will be made to update and 
          sumRange.
'''
#Difficulty: Medium
#15 / 15 test cases passed.
#Runtime: 892 ms
#Memory Usage: 30.8 MB

#Runtime: 892 ms, faster than 100.00% of Python3 online submissions for Range Sum Query - Mutable.
#Memory Usage: 30.8 MB, less than 93.37% of Python3 online submissions for Range Sum Query - Mutable.

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = sum(nums)

    def update(self, i: int, val: int) -> None:
        if val >= self.nums[i]:
            self.sum += abs(self.nums[i] - val)
        else:
            self.sum -= abs(self.nums[i] - val)
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        left_side = sum(self.nums[:i])
        right_side = sum(self.nums[j+1:])
        return self.sum - left_side - right_side


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)