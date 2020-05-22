"""
    Given two arrays of integers nums and index. Your task is to create target 
    array under the following rules:
        - Initially target array is empty.
        - From left to right read nums[i] and index[i], insert at index index[i] 
        the value nums[i] in target array.
        - Repeat the previous step until there are no elements to read in nums 
        and index.
    Return the target array.
    It is guaranteed that the insertion operations will be valid.
  
    Example:
    Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
    Output: [0,4,1,3,2]
    Explanation:
    nums       index     target
    0            0        [0]
    1            1        [0,1]
    2            2        [0,1,2]
    3            2        [0,1,3,2]
    4            1        [0,4,1,3,2]

    Constraints:
       - 1 <= nums.length, index.length <= 100
       - nums.length == index.length
       - 0 <= nums[i] <= 100
       - 0 <= index[i] <= i
"""
#Difficulty: Easy
#44 / 44 test cases passed.
#Runtime: 20 ms
#Memory Usage: 13.8 MB

#Runtime: 20 ms, faster than 99.65% of Python3 online submissions for Create Target Array in the Given Order.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i, pos in enumerate(index):
            result.insert(pos, nums[i])
        return result
